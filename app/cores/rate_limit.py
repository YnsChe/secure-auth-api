""" Defining different rate limiting types for routes"""

from pyrate_limiter import Duration, Limiter, Rate
from fastapi_limiter.depends import RateLimiter
from fastapi import Request, HTTPException, status

from threading import Lock
from time import monotonic

login_limiter = Limiter(Rate(3, Duration.MINUTE))
LOGIN_RATE_LIMIT = RateLimiter(login_limiter)

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {} # key -> {"window_start": float, "count": int}
        self.lock = Lock()


    def is_allowed(self, key: str)-> bool:
        with self.lock: # lock the resources
            now = monotonic() # get current time in seconds
            entry = self.requests.get(key) # check if the key exists in the dictionary

            # If the entry is empty --> first request of the client
            if entry is None:
                self.requests[key] = {"window_start": now, "count": 1} # set the window up
                return True

            # Otherwise get the window information
            window_start = entry["window_start"]
            count = entry["count"]
            elapsed = now - window_start # How long has passed since the last request

            if elapsed < self.window_seconds: # We check if we still in the same window
                if count >= self.max_requests: # If the number of max Requests is exceeded
                    return False
                entry["count"] += 1
                return True

            # otherwise reset the window
            entry["window_start"] = now
            entry["count"] = 1
            return True

    async def __call__(self, request: Request):
        client_ip = request.client.host
        if not self.is_allowed(client_ip):
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded")


login_limit = RateLimiter(max_requests=3, window_seconds=120)





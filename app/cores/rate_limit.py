from pyrate_limiter import Duration, Limiter, Rate
from fastapi_limiter.depends import RateLimiter

login_limiter = Limiter(Rate(3, Duration.MINUTE))
LOGIN_RATE_LIMIT = RateLimiter(login_limiter)
# Project Overview

This project is a backend authentication system built with FastAPI.

The project demonstrates following concepts:

* authentication flows
* password hashing and verification
* layered backend architecture
* database integration
* separation of concerns
* backend security fundamentals

---

# Structure (Layered Architecture)

```bash
secure-auth-api/
│
├── app/
│   ├── api/                 # routes and API endpoints
│   │   └── routes.py
│   │
│   ├── services/            # business logic
│   │   ├── auth_service.py
│   │   └── user_management.py
│   │
│   ├── core/                # security and configuration
│   │   └── hash.py
│   │
│   ├── db/                  # database logic
│   │   └── database.py
│   │
│   ├── models/              # data models
│   │   └── user.py
│   │
│   └── main.py              # application entry point
│
├── pyproject.toml           # dependencies and project configuration
└── README.md
```

---

# Current Features

* User registration
* User login
* Get users
* Delete user
* Password hashing and verification
* SQLite database integration

---

# How to Start

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Start the development server

```bash
fastapi dev app/main.py
```

The server will start at:

```bash
http://127.0.0.1:8000
```

API documentation is available at:

```bash
http://127.0.0.1:8000/docs
```

---

# Future Improvements

* structured error handling
* input validation
* JWT/session authentication
* protected routes
* login monitoring
* security logging

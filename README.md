# Project Overview

This project is a backend authentication system built with FastAPI.

The project demonstrates following concepts:

* authentication flows
* password hashing and verification
* layered backend architecture
* database integration
* separation of concerns
* backend security fundamentals

# Goal of the project

The goal of the project is to build an api authentication app and make it as secure as possible while demonstrating different concepts of authentication, user management and security.

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

## 2. Start the app

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

* Testing
* JWT/session authentication
* protected routes
* login monitoring
* security logging

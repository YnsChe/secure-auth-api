# Project Overview

This project is a backend authentication system built with FastAPI.

It demonstrates:

* Basic authentication flows
* Password hashing and verification (Argon2)
* Layered backend architecture
* Database integration with SQLite
* Separation of concerns
* backend security fundamentals

## Goal of the project

The goal is to build an API-based authentication service and make it as secure as reasonably possible while demonstrating different concepts of authentication, user management, and security.

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
│   ├── models/              # pydantic data models
│   │   └── user.py
│   │
│   └── main.py              # application entry point
│
├── pyproject.toml           # project configuration
├── requirements.txt         # python dependencies  
└── README.md
```

---

# Current Features

* User registration
* User login
* List users
* Delete user
* Password hashing and verification
* SQLite database integration

---

# How to Start

## 1. Install dependencies
Using FastAPI CLI:
```bash
pip install .
```
Or using uvicorn:
```bash
pip install -r requirements.txt
```

## 2. Start the app
Using fastapi CLI:
```bash
fastapi dev app/main.py
```
Or using uvicorn:
```bash
uvicorn --reload app.main:app 
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

* Automated tests
* JWT/session authentication
* protected routes
* login monitoring
* Security logging

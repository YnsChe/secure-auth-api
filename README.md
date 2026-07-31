# Project Overview

This project is a backend authentication system built with FastAPI.

It demonstrates:

* Basic authentication flows
* Password hashing and verification (Argon2)
* Layered backend architecture
* Database integration with SQLite
* Separation of concerns
* OAuth2 using JWT

## Goal of the project

The goal is to build an API-based authentication service and make it as secure as reasonably possible while demonstrating different concepts of authentication, user management, and security.

## Structure (Layered Architecture)

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
│   │   ├── authentication.py
│   │   └── hash.py
│   │
│   ├── db/                  # database logic
│   │   └── database.py
│   │
│   ├── models/              # pydantic data models
│   │   ├── tokens.py
│   │   └── user.py
│   │
│   └── main.py              # application entry point
│
├── pyproject.toml           # project configuration
├── requirements.txt         # python dependencies  
└── README.md
```

---

## Current Features

* User registration
* User login
* List users
* Delete user
* Password hashing and verification
* SQLite database integration

---

## How to Start

### 1. Install dependencies
Using FastAPI CLI:
```bash
pip install .
```
Or using uvicorn:
```bash
pip install -r requirements.txt
```
### 2. Start the app
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

---

## How to Test

### 1. Register a user
 - Method: POST
 - URL: http://127.0.0.1:8000/register/
 - Body (raw JSON):
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```

### 2. Login a user
 - Method: POST
 - URL: http://127.0.0.1:8000/login/
 - Body (raw JSON):
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```
 - The responce contains:
   ```bash
      {
        "access_token": "<JWT_TOKEN>",
        "token_type": "bearer"
      }
   ```
### 3. Access a protected Endpoint
 - Login and copy the returned <JWT_Token>
 - Mehtod: GET
 - URL: http://127.0.0.1:8000/protected/
 - Go to Authorization choose Bearer Token in Auth Type and past the <JWT_Token>
 - If the Token is still valid you will get your username in responce
 
For more Infos you can find the API documentation at:

```bash
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Automated tests
* User freindly GUI
* protected routes
* login monitoring
* Security logging

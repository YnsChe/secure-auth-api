# Project Overview

This project is a backend authentication system built with **FastAPI**.

It demonstrates:

* Basic authentication flows (register, login, protected endpoints)
* Password hashing and verification using **Argon**
* Layered backend architecture (API, services, core, database, models)
* Database integration with **SQLite**
* Raw SQL commands for user management
* Separation of concerns and clean code structure
* OAuth2-based authentication using **JWT** bearer tokens.

---

## Goal of the project

The goal is to build an API-based authentication service and make it as secure as reasonably possible while demonstrating different concepts of authentication, user management, and security.

---

## Technology Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **Authentication:** OAuth2, JWT
- **Password hashing:** Argon2
- **Data models:** Pydantic
- **Server:** Uvicorn (ASGI)

---

## Project Structure (Layered Architecture)

```bash
secure-auth-api/
│
├── app/
│   ├── api/                 # routes and API endpoints
│   │   └── routes.py
│   │
│   ├── services/            # business logic
│   │   ├── auth_service.py
│   │   └── user_service.py
│   │
│   ├── core/                # security and configuration
│   │   ├── authentication.py
│   │   └── hashing.py
│   │
│   ├── db/                  # database logic
│   │   └── database.py
│   │
│   ├── models/              # pydantic data models
│   │   ├── tokens.py
│   │   └── users.py
│   │
│   └── main.py              # application entry point
│
├── pyproject.toml           # project configuration
├── requirements.txt         # Python dependencies  
└── README.md
```

---

## Current Features

* User registration
* User login (OAuth2 + JWT)
* Role-based access control
* List users 
* Delete user (only admins)
* Password hashing and verification (Argon2)
* SQLite database integration
* Basic protected endpoints requiring a valid JWT

---

## How to Start

### 1. Install dependencies
Using "pyproject.toml":
```bash
pip install .
```
Or using "requirements.txt":
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
uvicorn app.main:app --reload
```
The server will start at:

```bash
http://127.0.0.1:8000
```

---

## API Usage

### 1. Register a user
 - Method: POST
 - URL: http://127.0.0.1:8000/register/
 - Body (JSON):
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```

### 2. Login a user
 - Method: POST
 - URL: http://127.0.0.1:8000/login/
 - Body (JSON):
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```
 - Response:
   ```bash
      {
        "access_token": "<JWT_TOKEN>",
        "token_type": "bearer"
      }
   ```
### 3. Access a protected Endpoint
 - Login and copy the returned **<JWT_Token>** from the login response.
 - Mehtod: GET
 - URL: http://127.0.0.1:8000/protected/
 - Add the token as a **Bearer token** in the "Autorization" header:
```bash
Authorization: Bearer <JWT_TOKEN>
```
 
## API Documentation

FastAPI automatically provides interactive documentation via Swagger UI:

```bash
http://127.0.0.1:8000/docs
```
or 
```bash
http://127.0.0.1:8000/redoc
```
---

## Future Improvements

* Automated tests (unit and integration tests using pytest)
* User-friendly GUI (React-based frontend for registration and login)
* Login monitoring and security logging
* Dockerization for easier deployment
* CI/CD pipeline for automated builds and tests

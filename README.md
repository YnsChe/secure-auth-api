## Project Overview

The project is being developed in three main stages:
1. **Build**: Build and test the authentication system and establish a solid baseline.

2. **Offensive Security**: Use the API as a security lab and try to find weaknesses in areas such as authentication, authorization, input validation, JWT handling, rate limiting, and business logic.

3. **Defensive Security**: Analyze the vulnerabilities found during testing, implement appropriate fixes, and add tests to make sure the vulnerabilities cannot easily return.

The idea is to go through the cycle of: Build → Attack → Fix → Retest

## Project Goals

The main goals of this project are to:
- Build a clean authentication API with FastAPI
- Learn and apply common authentication and authorization concepts
- Practice offensice security skills
- Learn to identify, exploit and fix vulnerabilities

*The project is intended as a learning project and is not designed as a production authentication service.*

## Technology Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **Authentication:** OAuth2, JWT
- **Password hashing:** Argon2
- **Data models:** Pydantic
- **Server:** Uvicorn (ASGI)
- **Testing:** Pytest

## Project Structure

```text
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
├── tests/
├── pyproject.toml           # project configuration
├── requirements.txt         # Python dependencies  
└── README.md
```
The application uses a layered structure to keep API routes, business logic, security logic and database access seperated.


## Current Features

* User registration and login
* Password hashing with Argon2
* JWT authentication
* OAuth2 password flow
* Protected endpoints
* Role-based access control
* List users (admin only)
* Delete user (admin only)
* SQLite database
* Input validation with Pydantic
* Login rate limiting
* Basic automated tests

## Running the project

Install dependencies
```bash
pip install .
```
Or using "requirements.txt":
```bash
pip install -r requirements.txt
```
Start the development server:
```bash
fastapi dev app/main.py
```
The API will be available at:
```bash
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation at: 
```bash
http://127.0.0.1:8000/docs
```
ReDoc available at: 
```bash
http://127.0.0.1:8000/redoc
```

## Example Usage
Register
```http
POST /register/
Content-Type: application/json
{
"username": "testuser"
"password": "testpassword"
}
```
Login
```http
POST /login/
Content-Type: application/json
{
"username": "testuser"
"password": "testpassword"
}
```
The response contains a JWT access token
```json
{
"access_token": "<JWT_TOKEN>"
"token_type": "bearer"
}
```
Use this token to access protected endpoints. For example:
```http
GET /user/me
Authorization: Bearer <JWT_TOKEN>
```

## Testing
Run the tests with: 
```bash
pytest
```

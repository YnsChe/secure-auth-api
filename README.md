# Secure-auth-api
### Implementing a Seucre Authentification and User Management System


# Structure (Layered Architecture)
```bash
secure-auth-api/
   ├── app/
   │    ├── api/     # routes, endpoints
   │    │    └── routes.py
   │    ├── services/  # business, logic
   │    │    └── auth_service.py
   │    │    └── user_management.py      
   │    ├── cores/    # security, config
   │    │    └── hash.py
   │    ├── db/      # database
   │    │    └── database.py
   │    ├── models   # data structures
   │    │     └── user.py
   │    └── main.py  # main App
   │    
   │
   ├── pyproject.toml (deoendencies + project config)
   └── README.md
```

# How to start
After installing dependencies, run the command:
```
fastapi dev
```
The server starts at https://127.0.0.1:8000
Call https://127.0.0.1:8000/docs To see the app documentation

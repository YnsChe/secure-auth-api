# secure-auth-api
Implementing a Seucre Authentification and User Management System


# Structure (Layered Architecture)
```bash
secure-auth-api/
   ├── app/
   │    ├── api/     # routes, endpoints
   │    ├── service/  # business, logic   
   │    ├── core/    # security, config
   │    ├── db/      # database
   │    ├── models   # data structures
   │    │     └── user.py
   │    └── main.py
   │    
   │
   ├── pyproject.toml (deoendencies + project config)
   └── README.md
```

# How to start
fastapi dev
server starts at https://127.0.0.1:8000

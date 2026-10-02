FROM python:3.11-slim
WORKDIR /app

# Install system Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

#Copy the project configuration first
COPY pyproject.toml ./

# Install dependencies defined in pyproject.toml
RUN pip install --no-cache-dir .

# Now copy the rest of the application code
COPY . .

# Create a non privileged user to run the app
RUN useradd -m -u 1000 authuser && chown -R authuser:authuser /app
USER authuser

#Expose the port
EXPOSE 8000

# Strat the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# 1. Official Playwright image with system dependencies
FROM mcr.microsoft.com/playwright/python:v1.63.0-noble

# 2. Working directory inside the container
WORKDIR /app

# 3. Copy dependencies and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy project files (respecting .dockerignore)
COPY . .

# 5. Default command executed on container startup
CMD ["pytest"]
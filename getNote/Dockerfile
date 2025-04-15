FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code and CA file
COPY . .

EXPOSE 5001

# Set environment variables if needed (e.g., for SSL connection)
# ENV SSL_CERT=/app/ca.pem

CMD ["python", "getNote.py"]

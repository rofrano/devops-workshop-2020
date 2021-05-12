FROM python:3.8-slim

# Establish a working folder
WORKDIR /app

# Establish dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source files last because they change the most
COPY service ./service

# Become non-root user
RUN useradd -m -r service && \
    chown -R service:service /app
USER service

# Run the service on port 5000
EXPOSE 5000
CMD ["gunicorn", "service:app", "--bind", "0.0.0.0:5000"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements (create this file if you don't have it)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script into the container
COPY email_notification.py .

# Set the default command to run your script
CMD ["python", "email_notification.py"]
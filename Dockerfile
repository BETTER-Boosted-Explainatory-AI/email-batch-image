# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy your script into the container
COPY email_notification.py .

# Install required Python packages
RUN pip install boto3

# Set the default command to run your script
CMD ["python", "email_notification.py"]
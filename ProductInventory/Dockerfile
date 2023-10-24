# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ProductInventory.settings

# Create and set the working directory
WORKDIR /app

# install required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Set the Environment variables
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD

# Expose the port the app runs on 8000
EXPOSE 8000

# Copy the entrypoint script into the container
COPY scripts/entrypoint.sh /entrypoint.sh
COPY scripts/wait-for-db.sh /wait-for-db.sh

# Make the script executable
RUN chmod +x /entrypoint.sh
RUN chmod +x /wait-for-db.sh

# Set the entry point to the script
ENTRYPOINT ["/entrypoint.sh"]
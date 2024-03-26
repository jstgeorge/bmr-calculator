# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Add the app directory contents into the container at /app
ADD ./app /app

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
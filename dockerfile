# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any required packages (if you add any external dependencies, list them in a requirements.txt file)
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the calculator application
CMD ["python", "calculator.py"]
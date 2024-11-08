# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /0x03-Unittests_and_integration_tests

# Copy the current directory contents into the container at /usr/src/app
COPY requirements.txt  .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x run_tests.py

# Run app.py when the container launches
CMD ["./run_tests.py"]

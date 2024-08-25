# Save this as Dockerfile
FROM python:3.9-slim

#Current working directory
WORKDIR /app


# Copy the requirements file to the container
COPY requirements.txt .


# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

#Run the application
CMD ["python", "app.py"]


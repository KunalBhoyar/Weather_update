# Save this as Dockerfile
FROM python:3.8-slim

#Current working directory
WORKDIR /app

#Copy the current dir code to the conatiner WORK dir
COPY . .

#Install Request
RUN pip install requests

#Run the application
CMD ["python", "weather_check.py"]

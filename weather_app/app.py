import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    api_key = os.getenv('WEATHER_API_KEY')  # Load the API key from environment variables

    if request.method == 'POST':
        city = request.form.get('city')
        
        if not city:
            error = "City name cannot be empty. Please enter a valid city name."
        elif not api_key:
            error = "No API key found! Please set the WEATHER_API_KEY environment variable."
        else:
            url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                if 'error' in data:
                    error = data['error'].get('message', 'An unknown error occurred. Please try again.')
                else:
                    weather = {
                        'city': data['location']['name'],
                        'temperature': data['current']['temp_c'],
                        'description': data['current']['condition']['text'],
                        'icon': data['current']['condition']['icon'],  # Weather icon URL
                        'wind_speed': data['current']['wind_kph'],
                        'humidity': data['current']['humidity'],
                        'feels_like': data['current']['feelslike_c']
                    }
            except requests.exceptions.RequestException as req_err:
                error = f"Request error occurred: {req_err}"

    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

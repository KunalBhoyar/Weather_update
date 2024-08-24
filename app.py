from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if not city:
            error = "City name cannot be empty. Please enter a valid city name."
        else:
            api_key = os.getenv('WEATHER_API_KEY') # Replace with your WeatherAPI key
            
            url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

            try:
                response = requests.get(url)
                response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
                data = response.json()

                # Check for errors in the API response
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
            except requests.exceptions.HTTPError as http_err:
                error = f"HTTP error occurred: {http_err}"
            except requests.exceptions.RequestException as req_err:
                error = f"Request error occurred: {req_err}"
            except ValueError:
                error = "Received an invalid response from the weather service."

    return render_template('index.html', weather=weather, error=error)
  


if __name__ == '__main__':
    app.run(debug=True)

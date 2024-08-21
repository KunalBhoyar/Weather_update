import requests
import os

def fetch_weather(api_key, city):
    """Fetches weather data for a specified city using WeatherAPI.com."""
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.json()

def check_conditions(weather_data, condition):
    """Checks if the specified weather condition exists in the weather data."""
    # Adjusting to the structure of the WeatherAPI.com response
    return condition in weather_data.get('current', {}).get('condition', {}).get('text', '')

def send_email(subject, body):
    """Placeholder function for sending an email."""
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    # Actual email sending logic would be implemented here

def main():
    api_key = os.environ.get('WEATHER_API_KEY')
    if not api_key:
        raise ValueError("No API key for WeatherAPI.com provided in environment variables.")

    city = 'Delhi'  # Change to the city of your choice
    try:
        weather_data = fetch_weather(api_key, city)
        if check_conditions(weather_data, 'Rain'):
            send_email('Rain Alert', 'It is going to rain today. Remember to bring an umbrella!')
        else:
            print("No rain predicted today.")
    except requests.RequestException as e:
        print(f"Failed to fetch weather data: {e}")

if __name__ == "__main__":
    main()

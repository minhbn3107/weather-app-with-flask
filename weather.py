from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()


def get_current_weather(city="Ho Chi Minh City"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={
        os.getenv("API_KEY")}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("Get Current Weather Conditions".center(80, "*"))

    city = input("Please enter a city name:\n")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Ho Chi Minh City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)

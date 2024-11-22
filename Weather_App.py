import streamlit as st
import requests
import json


def fetch_weather(city):
    """Fetch weather data from the API."""
    url = f"https://api.weatherapi.com/v1/current.json?key=43fb152c1e584163b64162705231507&q={city}"
    response = requests.get(url)
    return json.loads(response.text)

def main():
    st.set_page_config(
        page_title="Weather Report App",
        page_icon="☁️",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    st.title("Weather Report App ☁️🌞")

    # Custom CSS for styling the container
    st.markdown(
        """
        <style>
        .weather-container {
            border: 2px solid #4CAF50;
            border-radius: 15px;
            padding: 20px;
            background-color: #f9f9f9;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .weather-container h3 {
            color: #4CAF50;
        }
        .weather-container p {
            font-size: 16px;
            margin: 5px 0;
        }
        .weather-container .temp {
            font-size: 24px;
            font-weight: bold;
            color: #FF6347;
        }
        .weather-container .condition {
            font-size: 18px;
            color: #555;
        }
        .weather-container .last-updated {
            font-size: 14px;
            color: #888;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input field for city
    city = st.text_input("Enter your city name 🌍:")

    if city:
        # Fetch weather data
        weather_data = fetch_weather(city)

        # Extract relevant information
        temp_c = weather_data["current"]["temp_c"]
        temp_f = weather_data["current"]["temp_f"]
        condition = weather_data["current"]["condition"]["text"]
        time = weather_data["current"]["last_updated"]

        # Emojis for weather condition
        if "sun" in condition.lower():
            condition_emoji = "☀️"
        elif "cloud" in condition.lower():
            condition_emoji = "☁️"
        elif "rain" in condition.lower():
            condition_emoji = "🌧️"
        elif "snow" in condition.lower():
            condition_emoji = "❄️"
        else:
            condition_emoji = "🌤️"

        # Create a weather container with all details
        st.markdown(f"""
        <div class="weather-container">
            <h3>Weather Report for {city} {condition_emoji}</h3>
            <p class="temp">🌡️ Temperature: {temp_c}°C / {temp_f}°F</p>
            <p class="condition">Weather Condition: {condition} {condition_emoji}</p>
            <p class="last-updated">🕒 Last Updated: {time}</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



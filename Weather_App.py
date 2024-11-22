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
    st.title("☁️ Weather Report App")

    # Input field for city
    city = st.text_input("Enter your city name:")

    if city:
        # Fetch weather data
        weather_data = fetch_weather(city)
        
        # Extract relevant information
        temp_c = weather_data["current"]["temp_c"]
        temp_f = weather_data["current"]["temp_f"]
        condition = weather_data["current"]["condition"]["text"]
        time = weather_data["current"]["last_updated"]
        
        # Display weather information in a container
        st.markdown(f"""
        <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; margin-top: 20px; background-color: #f0f8ff;">
            <h2 style="color: #4CAF50; text-align: center;">Weather Report for {city}</h2>
            <p style="font-size: 20px; text-align: center;"><strong>Temperature:</strong> {temp_c}°C / {temp_f}°F</p>
            <p style="font-size: 20px; text-align: center;"><strong>Condition:</strong> {condition}</p>
            <p style="font-size: 20px; text-align: center;"><strong>Last Updated:</strong> {time}</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


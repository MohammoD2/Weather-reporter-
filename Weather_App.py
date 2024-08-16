import streamlit as st
import requests
import json
import pyttsx3

def fetch_weather(city):
    """Fetch weather data from the API."""
    url = f"https://api.weatherapi.com/v1/current.json?key=43fb152c1e584163b64162705231507&q={city}"
    response = requests.get(url)
    return json.loads(response.text)

def speak_weather_report(city, temp_c, temp_f, condition, time):
    """Convert weather report to speech."""
    engine = pyttsx3.init()
    report = (f"Now telling about the weather report of {city}. In {time}, "
              f"It's temperature is {temp_c} degrees Celsius or {temp_f} degrees Fahrenheit. "
              f"The weather of {city} is {condition}.")
    engine.say(report)
    engine.runAndWait()

def main():
    st.title("Weather Report App")

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

        # Display weather information
        st.write(f"### Weather Report for {city}")
        st.write(f"**Temperature:** {temp_c}°C / {temp_f}°F")
        st.write(f"**Condition:** {condition}")
        st.write(f"**Last Updated:** {time}")

        # Text-to-Speech button
        if st.button("Read Weather Report Aloud"):
            speak_weather_report(city, temp_c, temp_f, condition, time)
            st.success("Weather report is being read aloud!")

if __name__ == "__main__":
    main()






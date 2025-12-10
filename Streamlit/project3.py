import streamlit as st
import requests
import json

st.title("🌤️ Weather App")
city = st.text_input("Enter city or Country name:")

if st.button("Get Weather"):
    API_key = "c384c81d1252b8bb1b8a5f0ecd2d8da8"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        st.success(f"Weather in {city.capitalize()}:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature", f"{data['main']['temp']}°C")
        with col2:
            st.metric("Humidity", f"{data['main']['humidity']}%")
        with col3:
            st.metric("Wind Speed", f"{data['wind']['speed']}m/s")
        
        st.info(f"Description: {data['weather'][0]['description'].capitalize()}")

    else:
        st.error("❌ City not found! Please check the spelling and try again.")





















# 🌤️ Weather App

A simple weather application built with Streamlit that fetches real-time weather data.

## Features

- 🔍 Search weather by city name
- 🌡️ Current temperature (Celsius)
- 💧 Humidity percentage
- 💨 Wind speed
- 📝 Weather description

## Installation

```bash
pip install streamlit requests
```

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace `API_key` in the code with your key
3. Run the app:

```bash
streamlit run project3.py
```

4. Open `http://localhost:8501` in your browser

## Usage

1. Enter a city name
2. Click "Get Weather"
3. View the weather information

## Code Structure

```python
import streamlit as st
import requests

# Get user input
city = st.text_input("Enter city:")

# Fetch weather data from API
if st.button("Get Weather"):
    response = requests.get(URL)
    data = response.json()
    
    # Display results
    st.metric("Temperature", data['main']['temp'])
    st.metric("Humidity", data['main']['humidity'])
```

## API Used

[OpenWeatherMap API](https://openweathermap.org/api) - Free weather data

## Author

Created for learning Python and Streamlit

## License

MIT

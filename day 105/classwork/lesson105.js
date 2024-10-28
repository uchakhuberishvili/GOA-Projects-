

const axios = require('axios');

const fetchData = async (url) => {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
};

const fetchWeatherData = async (city) => {
    const apiKey = 'YOUR_OPENWEATHERMAP_API_KEY';
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    const weatherData = await fetchData(url);
    
    if (!weatherData) {
      return null;
    }
    
    const { main, weather } = weatherData;
    
    return {
        temperature: main.temp - 273.15,
        description: weather[0].description,
        icon: weather[0].icon,
    }};


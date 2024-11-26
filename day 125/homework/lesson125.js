import React, { useState, useEffect } from "react";

function WeatherApp() {
    const [city, setCity] = useState("");
    const [weather, setWeather] = useState(null);
    const [loading, setLoading] = useState(false);

    const fetchWeather = () => {
        if (city.trim()) {
            setLoading(true);
            fetch(`https://api.open-meteo.com/v1/forecast?current_weather=true&q=${city}`)
                .then((response) => response.json())
                .then((data) => {
                    setWeather(data.current_weather);
                    setLoading(false);
                })
                .catch(() => setLoading(false));
        }
    };

    return (
        <div>
            <h1>Weather App</h1>
            <input
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="Enter city"
            />
            <button onClick={fetchWeather}>Get Weather</button>
            {loading && <p>Loading...</p>}
            {weather && (
                <div>
                    <h2>Temperature: {weather.temperature}°C</h2>
                    <p>Condition: {weather.weathercode}</p>
                </div>
            )}
        </div>
    );
}

export default WeatherApp;

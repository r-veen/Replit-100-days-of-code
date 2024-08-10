import requests, json

latitude = 47.46497
longitude = 7.85174
timezone = "GMT"

result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}"
)

user = result.json()

weather_code_map = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    45: "Fog 🌫️",
    48: "Depositing rime fog 🌫️",
    51: "Drizzle: Light ☔",
    53: "Drizzle: Moderate ☔",
    55: "Drizzle: Dense intensity ☔",
    61: "Rain: Slight 🌧️",
    63: "Rain: Moderate 🌧️",
    65: "Rain: Heavy intensity 🌧️",
}

weather_code = user["daily"]["weathercode"][0]
max_temp = user["daily"]["temperature_2m_max"][0]
min_temp = user["daily"]["temperature_2m_min"][0]

weather_description = weather_code_map.get(weather_code,
                                           "Unknown Weather Code")

print(f"{weather_description}\n🥵 : {max_temp}\n🥶 : {min_temp}")

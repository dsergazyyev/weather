from enum import Enum

class WeatherType:  # Убрали наследование от Enum 
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

def print_weather_type(weather_type: WeatherType) -> None:
    print(weather_type)  # Вместо weather_type.value 

print_weather_type(WeatherType.CLOUDS)  # IDE подсветит ошибку типов
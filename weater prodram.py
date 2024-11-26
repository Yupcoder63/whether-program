import random

def generate_weather(city):
    temperatures = range(-10, 40)  # Possible temperatures from -10 to 40 degrees Celsius
    conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Stormy', 'Foggy']
    
    temperature = random.choice(temperatures)
    condition = random.choice(conditions)
    humidity = random.randint(20, 100)  # Random humidity percentage
    pressure = random.randint(950, 1050)  # Random atmospheric pressure in hPa
    
    report = {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "condition": condition
    }
    return report

def main():
    city = input("Enter city name: ")
    weather_report = generate_weather(city)
    
    print(f"Weather in {weather_report['city']}:")
    print(f"Temperature: {weather_report['temperature']}°C")
    print(f"Humidity: {weather_report['humidity']}%")
    print(f"Pressure: {weather_report['pressure']} hPa")
    print(f"Condition: {weather_report['condition']}")
    
if _name_ == "_main_":
    main()
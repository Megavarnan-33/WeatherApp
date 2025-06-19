import requests
city=input("Enter the city name: ") #Get the city name
API_KEY="5f31c8269d31d9c7b8a92d7644c7c0ef"
URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response=requests.get(URL)
if response.status_code == 200:
    data=response.json()
    print(f"Weather in {city}")
    print(f"Weather condition in {city} is: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}'C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Windspeed: {data['wind']['speed']} m/s")
else:
    print("City not found or Invalid api key")
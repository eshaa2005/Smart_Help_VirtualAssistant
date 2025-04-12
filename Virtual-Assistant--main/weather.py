# my user agent is : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)

import requests

def Weather():
    api_key = "cbb70d67e78901c0dc4a27c9cb2fea3e"  # Replace with your OpenWeather API key
    city = "Patna"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    try:
        data = response.json()

        if response.status_code != 200:
            return f"Error: {data.get('message', 'Unknown error')}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{temp}°C, {desc.capitalize()}"
    
    except Exception as e:
        return f"Weather API Error: {str(e)}"

# Test it before adding to your bot
print(Weather()) 

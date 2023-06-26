from urllib import response
import requests, json

baseURL="https://api.openweathermap.org/data/2.5/weather?"
apiID="a12e734df59bf6f7eff9aab439424852"
city = "Surrey"

def get_weat():
    URL=baseURL+"q="+city+"&appid="+apiID
    response=requests.get(URL)
    if response.status_code ==200:
        data=response.json()
        main=data["main"]
        temp=(main["temp"]-273)*1.8+32
        report=data["weather"]
        weatherDes=report[0]["description"]
        return weatherDes


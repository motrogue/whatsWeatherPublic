from operator import length_hint
import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])


        print(f'Погода в городе: {city}\nТемпература: {cur_weather}C°\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nСкорость ветра: {wind} м/с.\nВосход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}')


    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main ():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
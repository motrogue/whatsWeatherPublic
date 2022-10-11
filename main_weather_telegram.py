from dataclasses import replace
import requests
import datetime
import aiogram
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! напиши мне название города и я пришлю сводку погоды!')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()


        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])


        await message.reply(f'Погода в городе: {city}\nТемпература: {cur_weather}C°\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nСкорость ветра: {wind} м/с.\nВосход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}')


    except:
        await message.reply('\U00002620 Проверьте название города \U00002620')

if __name__ == '__main__':
    executor.start_polling(dp)
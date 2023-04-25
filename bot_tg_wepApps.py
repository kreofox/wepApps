from aiogram import Bot 
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot("TOKEN")
dp = Dispatcher(bot)

@dp.message_handler(commands="shop")
async def shop(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("shop", web_app=WebAppInfo(url = "https://") ))
    await message.answer("", reply_markup=markup)


@dp.message_handler(content_types=["web_app_data"])
async def wep_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')
    


executor.start_polling(dp)

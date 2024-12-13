from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.types import Message
from saber_pars import saber, saber_pars
from keyboards import *
from config import *
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN, parse_mode='html')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    await message.answer(f'salom <b>{full_name}</b> saberga xush kelibsiz')
    await show_category_saber(message)
    await information_ob_havo(message)



async def show_category_saber(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'kategoriyani tanlekng', reply_markup=buttons_category())


@dp.message_handler(content_types=['text'])
async def get_product_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_product = saber(get_value(category_text))

    for product in get_product:
        images = product.get('images')
        title = product.get('title')
        products = product.get('products')
        many = product.get('many')
        link = product.get('link')

        await message.answer_photo(photo=images, caption=f""""
{title}\n

{products}\n

{many}""", reply_markup=button_link(link))




executor.start_polling(dp)
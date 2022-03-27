from aiogram import types, Dispatcher
from create_bot import bot
from keybords import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Скоро здесь что-нибудь будет...', reply_markup=kb_client)
        await message.delete()
    except:
        await  message.reply('Общение с ботом через ЛС, напишите ему:\n@pittca_bot')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Доставка работает 24/7, 7 дней в неделю.')


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для вас это ненужная информация.\nМы готовы доставить ваш заказ в любую точку города.')

async  def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['schedule'])
    dp.register_message_handler(pizza_place_command, commands=['location'])
    dp.register_message_handler(pizza_menu_command,commands=['menu'])

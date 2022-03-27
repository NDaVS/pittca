from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/schedule')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/menu')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Поделиться местоположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5) ## add, insert

import logging
import os
import time

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup


storage=MemoryStorage()
# Replace 'BOT_TOKEN' with your actual bot token
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)


# Enable logging (optional but recommended)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Start command handler
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):

    markup = types.InlineKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer("Бот інфрмації")
    keyBoard1 = types.InlineKeyboardButton(text='📝Повістка', callback_data='notice')
    keyBoard2 = types.InlineKeyboardButton(text='❓Питання', callback_data='question')
    keyBoard3 = types.InlineKeyboardButton(text='💬Відповідь', callback_data='answer')
    markup.add(keyBoard1, keyBoard2, keyBoard3)
    await bot.send_message(message.from_user.id, 'Привіт,задайте питання,відповідь або місто вручення повістки',reply_markup=markup) #Работает только когда пзв-ль когдато писал боту
    

    row = int(message.message_id)
    inter = message.message_id - 1

    for row in range(inter):
        message_id = message.message_id - row
        await bot.delete_message(chat_id = message.from_user.id,message_id=message_id)
    



@dp.callback_query_handler(text='notice')
async def notice(callback: types.CallbackQuery):
    await callback.message.answer(f'вручення повістки у форматі починаючи: \n ! м/с.інформація \n знак оклику місто чи село(вибираєте м чи с) крапка назва '
                                'населеного пункту ,якщо село зазначаєте пишите район(можна скорочено:.р), далі по можливості вулиця(пиш-те: вул) крапка назва, і інформація \n Наприклад:\n'
                                '!м.Вінниця вул.Лесі Українки біля автовокзалу\n!с.Сороченці Віннецький.р біля школи №3')

@dp.callback_query_handler(text='question')
async def question(callback: types.CallbackQuery):
    await callback.message.answer(f'Задайте запитання у форматі приклад: \n ? ваше питання')

@dp.callback_query_handler(text='answer')
async def answer(callback: types.CallbackQuery):
    await callback.message.answer(f'Дайте відповідь на запитання у приклад: \n + ваша відповідь')






# Feedback message handler
@dp.message_handler(lambda message: message.text.startswith('!'))
async def notice(message: types.Message):
    # Extract the feedback text from the message
    time.sleep(3)
    notice_text = message.text.replace('!', '', 1).strip()

    # Send the feedback to the chat (replace 'YOUR_CHAT_ID' with the actual chat ID)
    chat_id = -1001979727750  # You can replace this with your specific chat ID
    await bot.send_message(chat_id, f"📝\n{notice_text}")

    # Optionally, you can store the feedback in a database or perform other actions here
    await message.answer("Дякуємо за вашу інформацію!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

    markup.add(types.KeyboardButton('/start'))
    await bot.send_message(message.from_user.id,'Викликати меню? Нажміть старт',reply_markup=markup)



@dp.message_handler(lambda message: message.text.startswith('?'))
async def question(message: types.Message):
    # Extract the feedback text from the message
    time.sleep(3)
    question_text = message.text.replace('?', '', 1).strip()

    # Send the feedback to the chat (replace 'YOUR_CHAT_ID' with the actual chat ID)
    chat_id = -1001979727750  # You can replace this with your specific chat ID
    await bot.send_message(chat_id, f"❓\n{question_text}")

    # Optionally, you can store the feedback in a database or perform other actions here
    await message.answer("Очікуйте можливу відповідь!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

    markup.add(types.KeyboardButton('/start'))
    await bot.send_message(message.from_user.id,'Викликати меню? Нажміть старт',reply_markup=markup)


@dp.message_handler(lambda message: message.text.startswith('+'))
async def answer(message: types.Message):
    # Extract the feedback text from the message
    time.sleep(3)
    answer_text = message.text.replace('+', '', 1).strip()

    # Send the feedback to the chat (replace 'YOUR_CHAT_ID' with the actual chat ID)
    chat_id = -1001979727750  # You can replace this with your specific chat ID
    await bot.send_message(chat_id, f"💬\n{answer_text}")

    # Optionally, you can store the feedback in a database or perform other actions here
    await message.answer("Дякуємо за вашу відповідь!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

    markup.add(types.KeyboardButton('/start'))
    await bot.send_message(message.from_user.id,'Викликати меню? Нажміть старт',reply_markup=markup)

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)



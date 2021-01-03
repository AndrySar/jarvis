from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


##

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Ваш Id: {0} \nИмя: {1}'.format(callback_query.from_user.id,
                                                           callback_query.from_user.username))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я персональный помощник J.A.R.V.I.S. Вы используете telegram версию. /help - "
                        "доступные команды")


help_message = text(
    "Доступные команды:\n",
    "/start - приветствие",
    "/whoami - Кто я?",
    "/help - команды",
    sep="\n"
)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message,
                        reply_markup=kb.help_buttons_panel)


if __name__ == '__main__':
    executor.start_polling(dp)

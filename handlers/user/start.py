from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.inline.user import language_markup
from states.user import RegisterState
from states.admin import CategoryState
from loader import dp, dbmanager, ADMINS
from utils.db_api.query import get_user_by_chat_id
from keyboards.default.admin import admin_category_markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    for admin in ADMINS:
        if int(admin) == chat_id:
            await message.answer("Hush kelibsiz admin. Tanlng", reply_markup=admin_category_markup)
            await CategoryState.choose_command.set()
        elif ADMINS[-1] == admin:
            dbmanager.connect()
            user = dbmanager.query_data_fetch_one(
                query_sql=get_user_by_chat_id, data=(chat_id,))
            dbmanager.close()
            if user:
                language = user[4]
                if language == "uz":
                    await message.answer(f"Hush kelibsiz <b>{user[1]}</b>")
                elif language == "ru":
                    await message.answer(f"Добро пожаловать, <b>{user[1]}</b>")
                elif language == "en":
                    await message.answer(f"Welcome <b>{user[1]}</b>")
            else:
                await state.update_data(chat_id=chat_id)
                await message.answer(f"""
<b>Quiz bot</b> ga xush kelibsiz {message.from_user.full_name}.
Добро пожаловать в <b>Quiz bot</b> {message.from_user.full_name}.
Welcome to <b>Quiz bot</b> {message.from_user.full_name}.""")
                await message.answer(f"""
Tilni tanlang!
Выберите язык!
Choose language!""", reply_markup=language_markup)
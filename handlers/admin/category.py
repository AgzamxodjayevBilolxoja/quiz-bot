from aiogram import types
from aiogram.dispatcher import FSMContext
from states.admin import CategoryState, QuestionState
from loader import dp, dbmanager
from utils.db_api.query import *
from keyboards.default.admin import category, question_markup, admin_category_markup

@dp.message_handler(state=CategoryState.choose_command)
async def choose_command_handler(message: types.Message, state: FSMContext):
    if message.text == "Kategoriya qo'shish":
        await message.answer("Kategoriya nomini o'zbekchada kiriting.")
        await CategoryState.category_uz.set()
    elif message.text == "Kategoriyalarni ko'rish":
        dbmanager.connect()
        categories = dbmanager.query_data_fetch_all(query_sql=get_categories)
        dbmanager.close()
        await state.update_data(categories=categories)
        category_markup = category(category_list=categories)
        await message.answer("Tanlang", reply_markup=category_markup)
        await CategoryState.show_category.set()


@dp.message_handler(state=CategoryState.category_uz)
async def get_uz_category_handler(message: types.Message, state: FSMContext):
    category_uz = message.text
    await state.update_data(category_uz=category_uz)
    await message.answer("Kategoriya nomini ruschada kiriting.")
    await CategoryState.category_ru.set()


@dp.message_handler(state=CategoryState.category_ru)
async def get_ru_category_handler(message: types.Message, state: FSMContext):
    category_ru = message.text
    await state.update_data(category_ru=category_ru)
    await message.answer("Kategoriya nomini inglizchada kiriting.")
    await CategoryState.category_en.set()


@dp.message_handler(state=CategoryState.category_en)
async def get_en_category_handler(message: types.Message, state: FSMContext):
    category_en = message.text
    await state.update_data(category_en=category_en)
    data = await state.get_data()
    dbmanager.connect()
    dbmanager.insert_data(insert_sql=insert_category, data=(
        data['category_uz'], data['category_ru'], data['category_en']))
    id = dbmanager.query_data_fetch_one(
        query_sql=get_category_id_by_name, data=(category_en,))
    dbmanager.close()
    await message.answer("Endi 1-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await state.update_data(category_id=id[0])
    await QuestionState.question1.set()

@dp.message_handler(state=CategoryState.show_category)
async def show_category_handler(message: types.Message, state: FSMContext):
    category_name = message.text
    if category_name == "Ortga":
        await message.answer("Tanlang", reply_markup=admin_category_markup)
        await CategoryState.choose_command.set()
    else:
        dbmanager.connect()
        categories = dbmanager.query_data_fetch_one(query_sql=get_category_by_name, data=(category_name,))
        questions = dbmanager.query_data_fetch_all(query_sql=get_questions_by_category_id, data=(categories[0],))
        lang = dbmanager.query_data_fetch_one(query_sql=get_lang_by_chat_id, data=(message.chat.id,))
        dbmanager.close()
        await state.update_data(lang=lang)
        await message.answer(f"Kategoriya ID si:{categories[0]}\nUZ:{categories[1]}\nRU:{categories[2]}\nEN:{categories[3]}", reply_markup=question_markup)
        await QuestionState.show_question.set()
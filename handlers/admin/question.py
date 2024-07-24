from aiogram import types
from aiogram.dispatcher import FSMContext
from states.admin import QuestionState, CategoryState
from loader import dp, dbmanager
from utils.db_api.query import insert_question, get_question_by_number
from keyboards.default.admin import admin_category_markup, category

@dp.message_handler(state=QuestionState.question1)
async def question1_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question1=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers1.set()

@dp.message_handler(state=QuestionState.answers1)
async def answers1_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers1=answers)
    await message.answer("Endi 1-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer1.set()

@dp.message_handler(state=QuestionState.correct_answer1)
async def correct_answer1_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer1=correct_answer)
    await message.answer("Endi 2-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question2.set()

@dp.message_handler(state=QuestionState.question2)
async def question2_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question2=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers2.set()

@dp.message_handler(state=QuestionState.answers2)
async def answers2_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers2=answers)
    await message.answer("Endi 2-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer2.set()

@dp.message_handler(state=QuestionState.correct_answer2)
async def correct_answer2_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer2=correct_answer)
    await message.answer("Endi 3-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question3.set()

@dp.message_handler(state=QuestionState.question3)
async def question3_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question3=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers3.set()

@dp.message_handler(state=QuestionState.answers3)
async def answers3_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers3=answers)
    await message.answer("Endi 3-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer3.set()

@dp.message_handler(state=QuestionState.correct_answer3)
async def correct_answer3_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer3=correct_answer)
    await message.answer("Endi 4-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question4.set()

@dp.message_handler(state=QuestionState.question4)
async def question4_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question4=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers4.set()

@dp.message_handler(state=QuestionState.answers4)
async def answers4_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers4=answers)
    await message.answer("Endi 4-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer4.set()

@dp.message_handler(state=QuestionState.correct_answer4)
async def correct_answer4_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer4=correct_answer)
    await message.answer("Endi 5-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question5.set()

@dp.message_handler(state=QuestionState.question5)
async def question5_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question5=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers5.set()

@dp.message_handler(state=QuestionState.answers5)
async def answers5_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers5=answers)
    await message.answer("Endi 5-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer5.set()

@dp.message_handler(state=QuestionState.correct_answer5)
async def correct_answer5_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer5=correct_answer)
    await message.answer("Endi 6-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question6.set()

@dp.message_handler(state=QuestionState.question6)
async def question6_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question6=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers6.set()

@dp.message_handler(state=QuestionState.answers6)
async def answers6_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers6=answers)
    await message.answer("Endi 6-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer6.set()

@dp.message_handler(state=QuestionState.correct_answer6)
async def correct_answer6_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer6=correct_answer)
    await message.answer("Endi 7-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question7.set()

@dp.message_handler(state=QuestionState.question7)
async def question7_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question7=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers7.set()

@dp.message_handler(state=QuestionState.answers7)
async def answers7_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers7=answers)
    await message.answer("Endi 7-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer7.set()

@dp.message_handler(state=QuestionState.correct_answer7)
async def correct_answer7_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer7=correct_answer)
    await message.answer("Endi 8-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question8.set()

@dp.message_handler(state=QuestionState.question8)
async def question8_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question8=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers8.set()

@dp.message_handler(state=QuestionState.answers8)
async def answers8_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers8=answers)
    await message.answer("Endi 8-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer8.set()

@dp.message_handler(state=QuestionState.correct_answer8)
async def correct_answer8_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer8=correct_answer)
    await message.answer("Endi 9-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question9.set()

@dp.message_handler(state=QuestionState.question9)
async def question9_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question9=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers9.set()

@dp.message_handler(state=QuestionState.answers9)
async def answers9_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers9=answers)
    await message.answer("Endi 9-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer9.set()

@dp.message_handler(state=QuestionState.correct_answer9)
async def correct_answer9_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer9=correct_answer)
    await message.answer("Endi 10-savolni namunagudek kiriting: Python - bu...;Python - это...;Python - is...\n3 tilda kiritishingiz kerak savollar orasida ; bo'lsin")
    await QuestionState.question10.set()

@dp.message_handler(state=QuestionState.question10)
async def question10_handler(message: types.Message, state: FSMContext):
    question = message.text
    await state.update_data(question10=question)
    await message.answer("Endi savolning javoblarini namunadigidek kiriting: 'Dasturlash tili','','';'Язык программирования','','';'Programming language','',''\njavoblarning orasini ; bilan ajrating.")
    await QuestionState.answers10.set()

@dp.message_handler(state=QuestionState.answers10)
async def answers10_handler(message: types.Message, state: FSMContext):
    answers = message.text
    await state.update_data(answers10=answers)
    await message.answer("Endi 10-savolning javobini namunadigidek kiriting: Dasturlash tili;Язык программирования;Programming language javoblarning orasini ; bilan ajrating.")
    await QuestionState.correct_answer10.set()

@dp.message_handler(state=QuestionState.correct_answer10)
async def correct_answer10_handler(message: types.Message, state: FSMContext):
    correct_answer = message.text
    await state.update_data(correct_answer10=correct_answer)
    data = await state.get_data()
    try:
        for i in range(1, 11):
            question = data[f'question{i}']
            question_split = str(question).split(";")
            uz_question = question_split[0]
            ru_question = question_split[1]
            en_question = question_split[2]
            answers = data[f'answers{i}']
            asnwers_split = str(answers).split(";")
            uz_answers = asnwers_split[0]
            ru_answers = asnwers_split[1]
            en_answers = asnwers_split[2]
            correct_answer = data[f'correct_answer{i}']
            correct_answer_split = str(correct_answer).split(";")
            uz_correct_answer = correct_answer_split[0]
            ru_correct_answer = correct_answer_split[1]
            en_correct_answer = correct_answer_split[2]
            dbmanager.connect()
            dbmanager.insert_data(insert_sql=insert_question, data=(i, "uz", data['category_id'], uz_question, uz_answers, uz_correct_answer))
            dbmanager.insert_data(insert_sql=insert_question, data=(i, "ru", data['category_id'], ru_question, ru_answers, ru_correct_answer))
            dbmanager.insert_data(insert_sql=insert_question, data=(i, "en", data['category_id'], en_question, en_answers, en_correct_answer))
            dbmanager.close()
            await message.answer("Tanlang", reply_markup=admin_category_markup)
            await state.finish()
    except Exception as ex:
        await message.answer("Savol qo'shishda xato.")
    await state.finish()

@dp.message_handler(state=QuestionState.show_question)
async def show_question_handler(message: types.Message, state: FSMContext):
    button_text = message.text
    data = await state.get_data()
    lang = data['lang']
    categories = data['categories']
    for i in range(1, 11):
        if button_text == "Ortga":
            await message.answer("Tanlang", reply_markup=category(category_list=categories))
            await state.finish()
            await CategoryState.show_category.set()
            break
        elif f"question{i}" == button_text:
            dbmanager.connect()
            question = dbmanager.query_data_fetch_all(query_sql=get_question_by_number, data=(i,))
            dbmanager.close()
            await message.answer(f"""
Til:{question[0][2]}
Kategoriya ID si:{question[0][3]}
Savol:{question[0][4]}
Javoblar:{question[0][5]}
To'g'ri javob:{question[0][6]}

Til:{question[1][2]}
Kategoriya ID si:{question[1][3]}
Savol:{question[1][4]}
Javoblar:{question[1][5]}
To'g'ri javob:{question[1][6]}

Til:{question[2][2]}
Kategoriya ID si:{question[2][3]}
Savol:{question[2][4]}
Javoblar:{question[2][5]}
To'g'ri javob:{question[2][6]}""")
    
create_user_table = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(55),
    phone_number VARCHAR(31) UNIQUE,
    chat_id BIGINT UNIQUE NOT NULL,
    lang VARCHAR(3) NOT NULL DEFAULT 'en'
    )"""

create_category_table = """CREATE TABLE IF NOT EXISTS category(
    id SERIAL PRIMARY KEY,
    uz VARCHAR(20) NOT NULL,
    ru VARCHAR(20) NOT NULL,
    en VARCHAR(20) NOT NULL)"""

create_question_table = """CREATE TABLE IF NOT EXISTS question(
    id SERIAL PRIMARY KEY,
    number_quest INTEGER NOT NULL,
    lang VARCHAR(3) NOT NULL,
    category_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answers TEXT NOT NULL,
    correct_answer VARCHAR NOT NULL)"""

insert_user = "INSERT INTO users(full_name,phone_number,chat_id,lang) VALUES(%s,%s,%s,%s)"

insert_category = "INSERT INTO category(uz, ru, en) VALUES(%s,%s,%s)"

insert_question = "INSERT INTO question(number_quest, lang, category_id, question, answers, correct_answer) VALUES(%s,%s,%s,%s,%s,%s)"

get_user_by_chat_id = "SELECT * FROM users WHERE chat_id=%s"

get_category_id_by_name = "SELECT id FROM category WHERE en=%s"

get_categories = "SELECT * FROM category"

get_category_by_name = "SELECT * FROM category WHERE uz=%s"

get_questions_by_category_id = "SELECT * FROM question WHERE category_id=%s"

get_question_by_number = "SELECT * FROM question WHERE number_quest=%s"

get_lang_by_chat_id = "SELECT lang FROM users WHERE chat_id=%s"

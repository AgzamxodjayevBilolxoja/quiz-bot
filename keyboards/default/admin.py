from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove_markup = ReplyKeyboardRemove()

admin_category_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kategoriya qo'shish"),
            KeyboardButton("Kategoriyalarni ko'rish")
        ]
    ], resize_keyboard=True
)

def category(category_list: list):
    category_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for category_tuple in category_list:
        category_markup.insert(KeyboardButton(f"{category_tuple[1]}"))
    category_markup.add("Ortga")
    return category_markup

question_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in range(1, 11):
    question_markup.insert(KeyboardButton(f"question{i}"))
question_markup.add("Ortga")

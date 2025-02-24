from aiogram import executor
from loader import dp,dbmanager
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.query import *

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    dbmanager.connect()
    dbmanager.create_table(create_table_sql=create_user_table)
    dbmanager.create_table(create_table_sql=create_category_table)
    dbmanager.create_table(create_table_sql=create_question_table)
    dbmanager.close()
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

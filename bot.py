from wiki_bot_commands import *
from logger import *
import asyncio
from aiogram import Bot, Dispatcher, types

# Объект бота
bot = Bot(token="5866449694:AAEE-pZ_sWeGv7VjCA1uMcwmCWqeBGrNov0")
dp = Dispatcher(bot)

print("Serv +")

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет, это второй бот, который я написал в рамках обучения программирования на языке "
                         "'Python'. Введи интересующий тебя термин в чат и получи его определение ;)")

@dp.message_handler(content_types=["text"])
async def hadle_text(message):
    await message.answer(wiki_search(message.text))
    log(message)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
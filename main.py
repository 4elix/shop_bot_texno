import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.commands import router_cmd
from handlers.text_user import router_txt


async def main() -> None:
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
        router_cmd, router_txt
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    print('START BOT !!!')
    asyncio.run(main())

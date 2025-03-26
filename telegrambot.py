import telegram
import asyncio
#from telegram import Update
#from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler
token = "7903260976:AAEQtnBt1kBNGxdidPx6cHreMo5QgDSEXpM"
chat_id =-1002411723910
bot = telegram.Bot(token)
loop = asyncio.get_event_loop() # 이벤트 루프를 얻음

async def send_message():
    await asyncio.sleep(1)
    loop.run_until_complete(bot.sendMessage(chat_id=chat_id, text="안녕하세요. 저는1 봇입니다."))
    loop.close
async def send_image():
    await asyncio.sleep(1)
    with open("Figure_1.png", "rb") as photo:
        loop.run_until_complete(bot.send_photo(chat_id=chat_id, photo=photo))
        loop.close
async def main():
    result=await send_image()
    print(result)

asyncio.run(main())
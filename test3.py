import telepot
TOKEN = '6638906640:AAHgV8_tCTBST_cXEZKCW-nnDUCWkbMpg3U'
bot = telepot.Bot(TOKEN)
chat_id = 6071498536
for i in range(10):
    bot.sendMessage(chat_id, "Hello")
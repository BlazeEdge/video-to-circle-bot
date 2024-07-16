import telebot
from config import *
from os import remove

bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, START_MSG)

@bot.message_handler(content_types=['video'])
def send_text(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('video.mp4', 'wb') as video:
        video.write(downloaded_file)
    bot.send_video_note(message.chat.id, open('video.mp4', 'rb'))
    remove('video.mp4')
    print('Video Sended!')

bot.infinity_polling()

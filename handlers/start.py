from loader import bot
from utils.logger import logger

@bot.message_handler(commands=['start'])
def start_message(message):
    logger.warning(f'{message.from_user.username} — команда START')

    msg = f"Старт"
    bot.send_message(message.chat.id, msg)

from loader import bot
from utils.logger import logger


@bot.message_handler(state=None)
def bot_echo(message):
    """ Вызывается, когда пользователь без состояния вводит несуществующую команду """

    if message.text:
        logger.warning(f'{message.from_user.username} — ECHO — {message.text}')
        bot.reply_to(
            message, f"Такой команды нет: {message.text}\n"
                     f"Нажмите /start, чтобы посмотреть весь список команд"
        )


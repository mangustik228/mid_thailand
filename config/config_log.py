from .config import config
from loguru import logger
from telebot import TeleBot



logger.add(
    config.logs.sink, 
    level=config.logs.level,
    rotation=config.logs.rotation,
    format=config.logs.format)


def send_message_tg(message:str):
    bot = TeleBot(config.bot.token)
    bot.send_message(config.bot.my_id, message[:500])

if config.alert:
    logger.level('ALERT', no=39, color="<green>")
    logger.add(send_message_tg, level="ALERT", format='{message}')

logger.info(f'Проект настроен')


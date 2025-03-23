import telebot
import os
import logging
from bot_logic import flip_coin  # Импортируем функции из bot_logic

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = os.getenv('BOT_TOKEN', '7808019428:AAF0jVT1acRQ62yB_G-vk8YLIn5tyqJeSJg')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, "Приветик! Я твой Telegram бот. Напиши команду /wb_artikuls, /tgk_Lika, /coin, /tex_podderhka.")
    except Exception as e:
        logger.error(f"Ошибка в send_welcome: {e}")

@bot.message_handler(commands=['tgk_Lika'])
def send_tgk(tgk):
    try:
        bot.reply_to(tgk, "https://t.me/linix_380.")
    except Exception as e:
        logger.error(f"Ошибка в send_tgk: {e}")

@bot.message_handler(commands=['wb_artikuls'])
def send_tgk(wb):
    try:
        bot.reply_to(wb, "https://t.me/65263048-арома расчёска , 162213264-тюлень Виталий , 287938313- наборчик с мармеладом харибо , 263793310-уходовые средства Егора Крида , 241180751-ой...")
    except Exception as e:
        logger.error(f"Ошибка в send_wb: {e}")



@bot.message_handler(commands=['coin'])
def send_coin(message):
    try:
        coin = flip_coin()
        bot.reply_to(message, f"Монетка выпала так: {coin}")
    except Exception as e:
        logger.error(f"Ошибка в send_coin: {e}")


@bot.message_handler(commands=['tex_podderhka'])
def send_tgk(tex):
    try:
        bot.reply_to(tex, "я-разработчик этого бота. В тех поддержку или для просьбы дополнений в боте писать мне в личные сообщения, или владельцу канала в тг")
    except Exception as e:
        logger.error(f"Ошибка в tex: {e}")


# Запуск бота
if __name__ == '__main__':
    logger.info("Бот запущен")
    bot.polling(none_stop=True)

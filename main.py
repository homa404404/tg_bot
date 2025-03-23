import telebot
import os
import logging
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = os.getenv('BOT_TOKEN', '7680128280:AAErh1tDaAxxG175WCPS-5Ji2RQagBVtTT0')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin также можешь скинуть фото разрабу этого бота дл яэтого просто скинь любое фото")
    except Exception as e:
        logger.error(f"Ошибка в send_welcome: {e}")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    try:
        bot.reply_to(message, "Привет! Как дела?")
    except Exception as e:
        logger.error(f"Ошибка в send_hello: {e}")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    try:
        bot.reply_to(message, "Пока! Удачи!")
    except Exception as e:
        logger.error(f"Ошибка в send_bye: {e}")

@bot.message_handler(commands=['pass'])
def send_password(message):
    try:
        password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
        bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")
    except Exception as e:
        logger.error(f"Ошибка в send_password: {e}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    try:
        emodji = gen_emodji()
        bot.reply_to(message, f"Вот эмоджи: {emodji}")
    except Exception as e:
        logger.error(f"Ошибка в send_emodji: {e}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    try:
        coin = flip_coin()
        bot.reply_to(message, f"Монетка выпала так: {coin}")
    except Exception as e:
        logger.error(f"Ошибка в send_coin: {e}")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = f"{message.from_user.id}_{file_info.file_id}.jpg"
        with open(file_name, 'wb') as new_file:
            new_file.write(bot.download_file(file_info.file_path))
        bot.reply_to(message, f"Фото сохранено как {file_name}")
    except Exception as e:
        logger.error(f"Ошибка в handle_photo: {e}")

if __name__ == "__main__":
    try:
        logger.info("Бот запущен")
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")

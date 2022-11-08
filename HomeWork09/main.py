
import logging # модуль

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
# bassicConfig - метод для настроики введения логов
logging.basicConfig( filename='my_log', filemode='a', encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
# format - параметр формата сообщений
# level - параметр, где мы мы указываем уровень важности (severity: DEBUG, 
#                                                                    INFO, 
#                                                                    WARNING, 
#                                                                    ERROR, 
#                                                                    CRITICAL)
# Атрибуты LogRecord:
# %(asctime)s - время 2003-07-08 16:49:45,896
# %(name)s - имя регистратора, используемого для регистрации вызова
# %(levelname)s - имя уровня важности
# %(message)s - сообщение, которое записывается при вызове. 
# Пример  %(message)s:                                                         
#           logger.info("Пол %s: %s", user.first_name, update.message.text)
#           отобразится как Пол "имя клиента": "сообщение клиента"

# создаем объект класса logger
logger = logging.getLogger(__name__)


# Определяем константы этапов разговора
GENDER, AGE, LOCATION, BIO = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Boy', 'Girl', 'Other']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут профессор Бот. Я проведу с вами беседу. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Ты мальчик или девочка?',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return GENDER

# Обрабатываем пол пользователя
def gender(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо. Сколько тебе лет ?, или отправь /skip, если не хочешь отвечать на этот вопрос.',
        reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `AGE`
    return AGE

# Обрабатываем возраст пользователя
def age(update, _):
    # определяем пользователя
    user = update.message.from_user
    user_answer = update.message.text
    # Пишем в журнал сведения о возрасте
    logger.info("Пользователю %s: %s лет", user.first_name, user_answer)
    # Отвечаем на сообщение с возрастом
    update.message.reply_text(
        'Отлично! С какой ты страны ?'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /skip для возраста
def skip_age(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о возрасте
    logger.info("Пользователь %s не отправил свой возраст.", user.first_name)
    # Отвечаем на сообщение с пропущенным сообщением о возрасте
    update.message.reply_text(
        'У каждого свои причины скрывать свои возраст. С какой ты страны ?'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Страна в, которой проживает %s: %s", user.first_name, update.message.text)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO


# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("Token")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
            AGE: [MessageHandler(Filters.text, age), CommandHandler('skip', skip_age)],
            LOCATION: [
                MessageHandler(Filters.text, location)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()
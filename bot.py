from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
TOKEN = '7688880977:AAEieSr0nbdAKYeAgvYS76_pihHBqJCn5z8'

# Вопрос и варианты ответов
QUESTION = {
    "question": "У меня отвалилась жопа",
    "options": ["Да", "Нет"]
}

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем клавиатуру с вариантами ответов
    keyboard = [
        [InlineKeyboardButton(option, callback_data=option)] for option in QUESTION["options"]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем вопрос пользователю
    await update.message.reply_text(text=QUESTION["question"], reply_markup=reply_markup)

# Обработчик ответа
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user_answer = query.data

    # Обрабатываем ответ
    if user_answer == "Да":
        response_text = "Послушайте: https://music.yandex.ru/artist/10068540"
    else:
        response_text = "Посмотрите: https://youtu.be/R08G2J59CYQ?si=3bimEXPCzpoD72_x"

    # Отправляем результат пользователю
    await query.edit_message_text(text=response_text)

# Основная функция
def main() -> None:
    # Создаем приложение и передаем ему токен
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_answer))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
import telebot
from telebot import types

bot = telebot.TeleBot('7594244287:AAE_AAc_XbPtlFXy4iyX0-orm5QxsmsmQgU')
tasks = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("➕ Добавить задачу"))
    markup.add(types.KeyboardButton("📋 Показать задачи"))
    markup.add(types.KeyboardButton("❌ Удалить задачу"))
    
    bot.send_message(message.chat.id, "Привет! Я бот для управления задачами. Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "➕ Добавить задачу")
def add_task(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите текст задачи:")
    bot.register_next_step_handler(message, process_task_text)

def process_task_text(message):
    chat_id = message.chat.id
    task_text = message.text

    user_tasks = tasks.get(chat_id, [])
    user_tasks.append(task_text)
    tasks[chat_id] = user_tasks

    bot.send_message(chat_id, f"Задача добавлена: {task_text}")

@bot.message_handler(func=lambda message: message.text == "📋 Показать задачи")
def show_tasks(message):
    chat_id = message.chat.id
    user_tasks = tasks.get(chat_id, [])

    if not user_tasks:
        bot.send_message(chat_id, "Ваш список задач пуст.")
        return

    task_list_text = "Ваши задачи:\n"
    for i, task in enumerate(user_tasks):
        task_list_text += f"{i + 1}. {task}\n"
    bot.send_message(chat_id, task_list_text)

@bot.message_handler(func=lambda message: message.text == "❌ Удалить задачу")
def delete_task(message):
    chat_id = message.chat.id
    user_tasks = tasks.get(chat_id, [])

    if not user_tasks:
        bot.send_message(chat_id, "Ваш список задач пуст. Нечего удалять.")
        return

    task_list_text = "Ваши задачи:\n"
    for i, task in enumerate(user_tasks):
        task_list_text += f"{i + 1}. {task}\n"
    bot.send_message(chat_id, task_list_text + "\nВведите номер задачи, которую хотите удалить:")
    bot.register_next_step_handler(message, process_delete_number)

def process_delete_number(message):
    chat_id = message.chat.id
    user_tasks = tasks.get(chat_id, [])

    try:
        task_number = int(message.text)
        if 1 <= task_number <= len(user_tasks):
            deleted_task = user_tasks.pop(task_number - 1)
            tasks[chat_id] = user_tasks
            bot.send_message(chat_id, f"Задача удалена: {deleted_task}")
        else:
            bot.send_message(chat_id, "Неверный номер. Попробуйте снова.")
    except ValueError:
        bot.send_message(chat_id, "Введите корректный номер задачи.")

if __name__ == '__main__':
    bot.infinity_polling()

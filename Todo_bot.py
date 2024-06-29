from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

tasks = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я Ваш бот для управления задачами. Используйте команды: "/add" - для добавления задачи, "/list" - для просмотра списка задач, "/done" - для отображения задачи как выполненной.')

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    task_description = ' '.join(context.args)
    if task_description:
        tasks.append({'description': task_description, 'done': False})
        await update.message.reply_text(f'Задача добавлена: {task_description}')
    else:
        await update.message.reply_text('Используйте команду /add <описание задачи>.')

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not tasks:
        await update.message.reply_text('Список задач пуст.')
        return

    message = 'Список задач:\n'
    for i, task in enumerate(tasks, start=1):
        status = '✔️' if task['done'] else '❌'
        message += f"{i}. {task['description']} - {status}\n"
    await update.message.reply_text(message)

async def mark_task_done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text('Используйте команду /done <номер задачи>.')
        return

    task_number = int(context.args[0])
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        await update.message.reply_text(f'Задача {task_number} отмечена как выполненная.')
    else:
        await update.message.reply_text('Неверный номер задачи.')

if __name__ == '__main__':
    application = Application.builder().token("7209919651:AAH20tXpW_EzkNvdVsMOoiYGl4kPgVmW9sI").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("list", list_tasks))
    application.add_handler(CommandHandler("done", mark_task_done))

    application.run_polling()

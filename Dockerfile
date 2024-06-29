# Используйте официальный образ Python
FROM python:3.10-slim

# Установите зависимости для Linux (если требуется)
RUN apt-get update && apt-get install -y build-essential

# Создайте виртуальное окружение
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Скопируйте файлы проекта
COPY . /app
WORKDIR /app

# Установите зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Укажите команду для запуска бота
CMD ["python", "Todo_bot.py"]

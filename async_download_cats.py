from pathlib import Path
import os
from datetime import datetime
import asyncio

import aiohttp
import aiofiles


http_proxy = os.getenv('http_proxy', None)
HTTP_PROXY = os.getenv('HTTP_PROXY', None)
PROXY = (http_proxy or HTTP_PROXY or None)

BASE_DIR = Path(__file__).parent

URL = 'https://api.thecatapi.com/v1/images/search'
CATS_DIR = CATS_DIR = BASE_DIR / 'cats'


# Асинхронная функция для получения нового изображения.
async def get_new_image_url():
    # Создать асинхронную сессию для выполнения HTTP-запроса.
    async with aiohttp.ClientSession() as session:
        # Выполнить асинхронный GET-запрос на указанный URL.
        response = await session.get(URL)
        # Асинхронно получить тело ответа в формате JSON.
        data = await response.json()
        # Извлечь URL случайного изображения из ответа.
        random_cat = data[0]['url']
        # Напечатать URL изображения.
        print(random_cat)
        # Вернуть URL изображения.
        return random_cat


# Главная асинхронная функция.
async def main():
    # Создать список задач для асинхронного выполнения.
    tasks = [
        # Асинхронно выполнить функцию get_new_image_url() 100 раз.
        asyncio.ensure_future(download_new_cat_image()) for _ in range(100)
    ]
    # Подождать, пока выполнятся все задачи.
    await asyncio.wait(tasks)


# Асинхронная функция для загрузки файла по URL.
async def download_file(url):
    filename = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        result = await session.get(url)
        # Здесь нужно использовать асинхронный контекстный менеджер.
        async with aiofiles.open(CATS_DIR / filename, 'wb') as f:
            # Перед методом записи нужно добавить ключевое слово await.
            await f.write(await result.read())


async def download_new_cat_image():
    url = await get_new_image_url()
    await download_file(url)


# Точка входа в программу.
if __name__ == '__main__':
    # Записать текущее время начала выполнения программы.
    start_time = datetime.now()
    
    # Получить текущий событийный цикл.
    loop = asyncio.get_event_loop()
    # Запустить основную корутину и подождать, пока она завершится.
    loop.run_until_complete(main())
    
    # Записать текущее время окончания выполнения программы.
    end_time = datetime.now()
    # Напечатать время выполнения программы.
    print(f'Время выполнения программы: {end_time - start_time}.')
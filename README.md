# Сто котиков каждому
Программа загружает сто картинок с котиками с сайта TheCatAPI, складывает эти файлы в одном месте и выводит список названий сохранённых файлов в терминал. 

## Установка
- Создать виртуальное окружение

Windows

```bash
python -m venv venv
```

Linux, OSX

```bash
python3 -m venv venv
```

- Активировать окружение

Windows

```bash
source ./venv/Scripts/activate
```

Linux, OSX

```bash
source ./venv/bin/activate
```

- Установить зависимости

```bash
pip install -r requirements.txt
```

## Запуск программы 

```bash
proxy=http://proxy.example.com:3128
export http_proxy="$proxy"
export https_proxy="$proxy"
export no_proxy="localhost,127.0.0.1"

python download_cats.py
```

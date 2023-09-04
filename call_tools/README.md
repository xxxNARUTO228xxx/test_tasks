### Задача
Лежит в task.md

### Запуск
Python 3.8.10

Веса для pocketsphinx [rus](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Russian/) и [eng](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/US%20English/). Указать путь к моделям в конфиге. 

Запуск приложения:
```
pip install -r requirements.txt
python main.py
```
Поднимется uvicorn server с fastapi на `{host}:{port}`, указанных в конфиге. Веб-интерфейс с доступными методами можно увидеть на `{host}:{port}/docs`

### Docker
```
docker build -t call_tools .
docker run -p 127.0.0.1:8000:8000 --name -d call_tools_service  call_tools
```

### Логирование
Логи будут появляться в папке `./logs`, 1 день = 1 логфайл, через 30 дней старый логфайл удаляется.
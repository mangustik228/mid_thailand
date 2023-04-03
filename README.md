### mid_thailand

Парсер посольства России в Тайланде.

```python
# utils/functions.py Необходимо заменить на свои id / cd
return 46483, "492D770A" 
```

```bash
# Файл .env, надо создать в корне
# id в телеграмм, куда будет приходить сообщения
my_id=000000 

# token вашего бота в телеграмм, который будет отправлять сообщения
bot_token=asdasdfasdfasdfasdfasdfasdf

# Token с сервиса CaptchaAi.com
captcha_token=737c52e19ee31805fbe35aa74e347520
```

## Запуск на сервере
Необходимо установить docker 

Порядок запуска: 
1. копируем репозиторий `git clone ...`
2. заходим в папку проекта 
3. выполняем команду `docker compose build` 
4. Пишем команду `crontab -e` 
    - дописываем в конце файла `*/50 * * * * docker compose -f /path/to/project/docker-compose.yml up -d` 
    - `*/50` указывает чтоб задача запускалась каждые 50минут









created: 2023-03-28 06:40  
author: Vasiliy_mangust228  
email: <a href="mailto:bacek.mangust@gmail.com">bacek.mangust@gmail.com</a>  
tg: https://t.me/mangusik228  
            
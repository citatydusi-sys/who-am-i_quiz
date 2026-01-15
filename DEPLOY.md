# Инструкция по деплою на Render

## Шаги для деплоя:

1. **Подключите репозиторий к Render:**
   - Зайдите на https://render.com
   - Создайте новый Web Service
   - Подключите репозиторий GitHub: `citatydusi-sys/who-am-i_quiz`

2. **Настройки Build & Deploy:**
   - **Name**: `english-quiz-app` (или любое другое имя)
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT`

3. **Environment Variables:**
   Добавьте следующие переменные окружения:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=who-am-i-quiz.onrender.com
   ```
   
   **ВАЖНО:** Замените `who-am-i-quiz.onrender.com` на ваш реальный домен Render!

4. **Генерация SECRET_KEY:**
   Вы можете сгенерировать новый SECRET_KEY командой:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **После деплоя:**
   - Render автоматически запустит build.sh
   - Миграции применятся автоматически
   - Данные импортируются через команду import_data
   - Статические файлы соберутся автоматически

## Примечания:

- Убедитесь, что файл `build.sh` имеет права на выполнение (chmod +x build.sh)
- Если возникнут проблемы, проверьте логи в панели Render
- База данных SQLite будет создана автоматически при первом запуске

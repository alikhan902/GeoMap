# Документация проекта «Куда пойти — Москва глазами Артёма"

## 0 Ссылка на опубликованный сайт

redas8080.pythonanywhere.com

## 1. Описание проекта

Проект представляет собой веб-приложение с интерактивной картой Москвы. Пользователь может выбрать место на карте, увидеть краткое описание, главную фотографию и пролистываемую галерею фотографий, а также детальное описание с HTML-разметкой.

Приложение использует Django для бэкенда

---

## 2. Стек технологий

- **Backend:** Django 5.2, Django REST Framework  
- **База данных:** SQLite (по умолчанию)  
- **Хранение медиа:** локальная папка `media/`  
- **Дополнительно:** CKEditor для WYSIWYG редактора в админке

---

## 3. Структура проекта

```
GeoMap/
│
├─ GeoMap/                  # Основной Django проект
│   ├─ settings.py          # Настройки проекта
│   ├─ urls.py              # Роутинг
│   └─ wsgi.py
│
├─ geoapp/                  # Приложение с моделями и API
│   ├─ models.py            # Place и PlaceImage
│   ├─ admin.py             # Настройка админки с Inline для PlaceImage
│   ├─ serializers.py       # DRF сериализаторы
│   ├─ views.py             # ViewSets для Place
│   └─ urls.py              # API маршруты
│
├─ frontend/                # Фронтенд-шаблоны (HTML, CSS)
│   └─ index.html           # Основная страница с картой
│
├─ media/                   # Загруженные изображения
└─ static/                  # Статические файлы (css, js, изображения)
```

---

## 4. Модели

### 4.1 Place

```python
class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    main_image = models.ImageField(blank=True, upload_to='places/')
```

### 4.2 PlaceImage

```python
class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
```

**Примечания:**
- В админке используется `TabularInline`, чтобы добавлять фотографии прямо при создании места.
- Для вывода фотографий в админке добавлен метод `image_preview`.

---

## 5. API

### 5.1 Список всех мест

```
GET /api/places/
```

**Ответ:**

```json
[
  [
    {
        "title": "text",
        "imgs": [
            "url",
            "url",...
        ],
        "description_short": "text",
        "description_long": "text",
        "coordinates": {
            "lat": float,
            "lng": float
        }
    },
  ...
]
```

## 6. Настройка и запуск

### 6.1 Установка зависимостей

```bash
pip install -r requirements.txt
```

### 6.2 Настройка `.env` (пример)

```env
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 6.3 Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6.4 Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 6.5 Запуск сервера

```bash
python manage.py runserver
```

- Карта доступна по `http://127.0.0.1:8000/`.  
- Админка по `http://127.0.0.1:8000/admin/`.  

---

## 7. Настройка админки

```python
from django.contrib import admin
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('title',)
```

- Inline позволяет добавлять несколько фотографий одновременно.  
- Можно использовать `image_preview` для отображения миниатюр.


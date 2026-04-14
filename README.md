



# Grocery Shop API Project

RESTful API для продуктового магазина, реализованный на Django Rest Framework. Проект включает в себя каталог товаров и функционал корзины для авторизованных пользователей.

## Структура проекта
```
├── .pytest_cache
│   ├── v
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── README.md
├── cart
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_cartitem_options.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── catalog
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_category_options_alter_product_options_and_more.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myshop
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tests
│   ├── conftest.py
│   ├── test_cart.py
│   └── test_catalog.py
├── .coverage
├── .gitignore
├── fixtures.json
├── manage.py
├── pytest.ini
├── requirements.txt
└── test._api.http
```

## Тестирование и качество кода
В соответствии с требованиями (норматив не менее **80%**), проект полностью покрыт автоматизированными тестами.
- **Инструментарий**: `pytest`, `pytest-django`, `pytest-cov`.
- **Методология**: Тесты реализованы по паттерну **Arrange-Act-Assert**.
- **Покрытие (Coverage)**: Достигнут показатель **87%**, что гарантирует стабильность работы ключевых узлов API.

**Запуск тестов:**
```
pytest
```
**Проверка покрытия:**
```
pytest --cov=.
```

## Дополнительные материалы
Ниже приведен список ресурсов, к которым я обращался в процессе разработки для решения специфических задач и настройки архитектуры проекта:

### Работа с изображениями
* [Transform Your Django Images with Django-ImageKit](https://pypi.org/project/django-imagekit/) — оптимизация медиа-файлов.
* [Django-ImageKit Documentation](https://django-imagekit.readthedocs.io/) — официальный справочник по библиотеке.

### Сериализация и DRF
* [Representing Foreign Key Values](https://www.django-rest-framework.org/api-guide/relations/) — способы представления связей в API.
* [DRF: FloatField](https://www.django-rest-framework.org/api-guide/fields/#floatfield) — специфика работы с числовыми полями.

### Оптимизация БД
* [Django: Query Expressions (F() expressions)](https://docs.djangoproject.com/en/stable/ref/models/expressions/) — вычисления на стороне базы данных.
* [GeeksforGeeks: Aggregate vs Annotate](https://www.geeksforgeeks.org/aggregate-vs-annotate-in-django/) — сравнение методов агрегации данных.

### Аутентификация и документация
* [Django: User authentication system](https://docs.djangoproject.com/en/stable/topics/auth/) — документация встроенной системы авторизации.
* [DRF: TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) — использование токенов доступа.
* [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/) — генерация схем OpenAPI 3 и Swagger.

## Инструкция по запуску
Для запуска проекта локально выполните следующие шаги:

1. **Установите зависимости**:
   ```
   pip install -r requirements.txt
   ```
2. **Примените миграции**:
   ```
   python manage.py migrate
   ```
3. **Загрузите демонстрационные данные**:
   ```
   python manage.py loaddata fixtures.json
   ```
4. **Запустите сервер**:
   ```
   python manage.py runserver
   ```
5. **Документация Swagger UI** доступна по адресу: `http://127.0.0.1:8000/api/docs/`

---
**Автор:** Максим Пинчук — MaksPinch (https://github.com/MaksPinch)

---



**Languages / Языки:**
* [English Edition](#english-edition)
* [Русская версия](#русская-версия)


---
<a name="english-edition"></a>

# Grocery Shop API Project

A robust RESTful API for a grocery store built with **Django Rest Framework**. The project features a comprehensive product catalog and shopping cart functionality for authenticated users.

## Project Structure
```
├── cart
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── catalog
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media
│   ├── categories
│   ├── products
│   └── subcategories
├── myshop
│   ├── settings.py
│   ├── urls.py
├── tests
│   ├── conftest.py
│   ├── test_algorithm.py
│   ├── test_cart.py
│   └── test_catalog.py
├── .coveragerc
├── .gitignore
├── README.md
├── algorithm_task.py
├── fixtures.json
├── manage.py
├── pytest.ini
├── requirements.txt
└── test._api.http
```

## Testing and Code Quality
In line with professional standards (minimum 80% requirement), the project is fully covered by automated tests.
- **Toolkit**: `pytest`, `pytest-django`, `pytest-cov`.
- **Methodology**: Tests follow the **Arrange-Act-Assert** pattern.
- **Code Coverage**: Achieved a **91% coverage** rate, ensuring the stability and reliability of the API's core logic.

**Run Tests:**
```bash
pytest
```
**Check Coverage:**
```bash
pytest --cov=.
```

## Key Resources & Documentation
The following resources were utilized during development for advanced architecture design and specific task implementations:

### Media Handling
* [Django-ImageKit](https://pypi.org/project/django-imagekit/) - Media file optimization.
* [ImageKit Docs](https://django-imagekit.readthedocs.io/) - Official reference for processing images.

### Serialization & Relations
* [Representing Foreign Key Values](https://www.django-rest-framework.org/api-guide/relations/) - Handling API relationship representations.
* [DRF: FloatField](https://www.django-rest-framework.org/api-guide/fields/#floatfield) - Specifics of numeric field handling.

### Database Optimization
* [Django: Query Expressions (F() expressions)](https://docs.djangoproject.com/en/stable/ref/models/expressions/) - Database-side calculations.
* [Aggregate vs Annotate](https://www.geeksforgeeks.org/aggregate-vs-annotate-in-django/) - Data aggregation and annotation logic.

### Authentication & API Docs
* [Django Authentication System](https://docs.djangoproject.com/en/stable/topics/auth/) - Core security and user management.
* [DRF: TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) - Secure API access tokens.
* [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/) - OpenAPI 3 and Swagger documentation generation.

## Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MaksPinch/django-shop-api.git
   cd django-shop-api
   ```

2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   ```
   **Activate (Windows):**
   ```bash
   venv\Scripts\activate
   ```
   **Activate (Mac/Linux):**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Load demo data**:
   ```bash
   python manage.py loaddata fixtures.json
   ```

6. **Start the server**:
   ```bash
   python manage.py runserver
   ```

7. **API Documentation**:
   Swagger UI is available at: `http://127.0.0.1:8000/api/docs/`

---
**Developer:** Maksim Pinchuk — [MaksPinch](https://github.com/MaksPinch)

---

<a name="русская-версия"></a>
# Grocery Shop API Project

RESTful API для продуктового магазина, реализованный на Django Rest Framework. Проект включает в себя каталог товаров и функционал корзины для авторизованных пользователей.

## Структура проекта
```
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
├── media
│   ├── categories
│   │   ├── products.jpeg
│   │   └── products_JED1uhv.jpeg
│   ├── products
│   │   ├── cottage_cheese.jpg
│   │   ├── cottage_cheese_JVqv0jh.jpg
│   │   ├── kefir-1.jpg
│   │   ├── kefir-1_Yfle4nl.jpg
│   │   ├── milk.png
│   │   └── milk_s88LQPq.png
│   └── subcategories
│       ├── dairy.jpg
│       └── dairy_XR4zjUY.jpg
├── myshop
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tests
│   ├── conftest.py
│   ├── test_algorithm.py
│   ├── test_cart.py
│   └── test_catalog.py
├── .coveragerc
├── .gitignore
├── README.md
├── algorithm_task.py
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
- **Покрытие (Coverage)**: Достигнут показатель **91%**, что гарантирует стабильность работы ключевых узлов API.

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
* [Transform Your Django Images with Django-ImageKit](https://pypi.org/project/django-imagekit/) - оптимизация медиа-файлов.
* [Django-ImageKit Documentation](https://django-imagekit.readthedocs.io/) - официальный справочник по библиотеке.

### Сериализация и DRF
* [Representing Foreign Key Values](https://www.django-rest-framework.org/api-guide/relations/) - способы представления связей в API.
* [DRF: FloatField](https://www.django-rest-framework.org/api-guide/fields/#floatfield) - специфика работы с числовыми полями.

### Оптимизация БД
* [Django: Query Expressions (F() expressions)](https://docs.djangoproject.com/en/stable/ref/models/expressions/) - вычисления на стороне базы данных.
* [GeeksforGeeks: Aggregate vs Annotate](https://www.geeksforgeeks.org/aggregate-vs-annotate-in-django/) - сравнение методов агрегации данных.

### Аутентификация и документация
* [Django: User authentication system](https://docs.djangoproject.com/en/stable/topics/auth/) - документация встроенной системы авторизации.
* [DRF: TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) - использование токенов доступа.
* [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/) - генерация схем OpenAPI 3 и Swagger.

## Инструкция по запуску
Для запуска проекта локально выполните следующие шаги:

1. **Клонируйте репозиторий**:
   ```
   git clone https://github.com/MaksPinch/django-shop-api.git
   ```
   ```
   cd django-shop-api
   ```
2. **Настройте виртуальное окружение**:
   ```
   python -m venv venv
   ```
   Активация (Windows)
   ```
   venv\Scripts\activate
   ```
   Активация (Mac/Linux)
   ```
   source venv/bin/activate
   ```

3. **Установите зависимости**:
   ```
   pip install -r requirements.txt
   ```
4. **Примените миграции**:
   ```
   python manage.py migrate
   ```
5. **Загрузите демонстрационные данные**:
   ```
   python manage.py loaddata fixtures.json
   ```
6. **Запустите сервер**:
   ```
   python manage.py runserver
   ```
7. **Документация Swagger UI** доступна по адресу: `http://127.0.0.1:8000/api/docs/`

---
**Автор:** Максим Пинчук — MaksPinch (https://github.com/MaksPinch)

---

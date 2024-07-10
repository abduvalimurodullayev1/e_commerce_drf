# E-Commerce Project with Django REST Framework

## Description

This project is an e-commerce platform built using Django REST Framework (DRF). It provides a backend API for managing products, categories, orders, and user favorites.

### Tavsif

Ushbu loyiha Django REST Framework (DRF) yordamida yaratilgan elektron savdo platformasi. Ushbu platforma mahsulotlar, kategoriyalar, buyurtmalar va foydalanuvchining sevimli mahsulotlarini boshqarish uchun backend API bilan ta’minlanadi.

### Описание

Этот проект - платформа электронной коммерции, созданная с использованием Django REST Framework (DRF). Он предоставляет API для управления товарами, категориями, заказами и избранными продуктами пользователей.

## Features

- User authentication and authorization with JWT tokens.
- CRUD operations for products and categories.
- Order management system.
- User favorites management.

### Xususiyatlar

- Foydalanuvchi autentifikatsiyasi va autorizatsiyasi JWT belgilari bilan.
- Mahsulotlar va kategoriyalar uchun CRUD amallari.
- Buyurtmalar boshqarish tizimi.
- Foydalanuvchining sevimli mahsulotlari boshqarish.

### Особенности

- Аутентификация и авторизация пользователей с помощью JWT токенов.
- CRUD операции для продуктов и категорий.
- Система управления заказами.
- Управление избранными продуктами пользователей.

## Technologies Used

- Python 3.10+
- Django 3.2+
- Django REST Framework 3.12+
- PostgreSQL (or your preferred database)
- Docker (optional, for containerization)

### Используемые технологии

- Python 3.10+
- Django 3.2+
- Django REST Framework 3.12+
- PostgreSQL (или другая база данных по вашему выбору)
- Docker (опционально, для контейнеризации)

## Installation

### Prerequisites

- Python installed (3.10 or higher)
- PostgreSQL installed (or another database supported by Django)

### Установка

#### Подготовка

1. Clone the repository:

   ```bash
   git clone https://github.com/abduvalimurodullayev1/e_commerce_drf.git
   cd e_commerce_drf


python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

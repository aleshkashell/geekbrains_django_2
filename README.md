# Geekbrains django

Репозиторий второй части курса django. Первая часть находится по адресу https://github.com/aleshkashell/geekbrains_django

## Оглавление

- [Урок 1. Отправка электронной почты. Контекстные процессоры](#Урок-1)
- [Урок 2. Регистрация через социальную сеть. Django-ORM: связь один-к-одному](#Урок-2)
- [Урок 3. Работа с заказом пользователя: CBV, Django formsets](#Урок-3)
- [Урок 4. Работа с заказом пользователя: обновляем остатки товара, добавляем код jQuery](#Урок-4)
- [Урок 5. Развертывание Django-проекта на сервере](#Урок-5)
- [Урок 6. Профилирование и нагрузочное тестирование проекта, оптимизация работы с базой данных](#Урок-6)
- [Урок 7. Еще быстрее: кеширование в Django](#Урок-7)

## Урок 1

- Добавлен acitvation_key в модель пользователя
- Настроена отправка email для подтверждения регистрации
- Сделана активация пользователя по ссылке из письма
- Создан контекстный процессор для получения товара из корзины
- Настроено отображения сообщения об успешной отправке письма при регистрации

## Урок 2

- Настроена регистрация через социальные сети Google и Вкотакте
- Настроена связь один к одному для моделей ShopUser и ShopUserProfile
- Создан pipeline для регистрации через социальную сеть
- Настроено заполение профиля при регистрации через социальные сети
- Настроена загрузка автарки при регистрации через социальную сеть
- Рассмотрена работа исключения AuthForbidden

## Урок 3

- Создано выпадающее меню на профиль пользователя и заказы
- Создано приложение ordersapp для работы с заказами пользователя
- Созданы котроллеры приложения ordersapp
- Деактивирована панель django debug toolbar
- Сделано обновление статуса заказа при совершении покупки
- Организована работа с заказами в админке

## Урок 4

- Организована работа с остатками
- Реализовано обновление статики через JQuery
- Настроен django-dynamic-formset
- Организовано асинхронное обноление цены и общих показателей при добавлении нового товара в заказ

## Урок 5

- Экспортированы данные из БД
- Проект подготовлен к postgre
- Проект подкотовлен к продакшену
- Подготовлен сервер
- Сконфигурирован nginx и сертификаты
- Проект доступен по адресу https://django.anominus.ru/

## Урок 6

- Установлено приложение django-debug-toolbar
- Визуализирована структура моделей при помощи django_extensions, созданы файлы geekshop_urls.txt и geekshop_visualized.png
- Установлена утилита siege и произведены замеры. Результаты сохранены в файле
- Исправлены ошибки доступа к адресам для незалониненых пользователей
- Проведено тестирование, в результате которого определены возможности сервера
- Произведена оптимизация БД, результаты занесены в таблицу

## Урок 7

- Рассмотрена работа @cached_property
- Рассмотрена работа кэширования в шаблонах
- Установлен и настроен memcached
- Реализовано и рассмотрена работы кэширования контроллеров
- Реализована работа элементов через ajax и кеширование элементов для него
- Рассмотрено кэширование всего сайта

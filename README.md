# Geekbrains django

Репозиторий второй части курса django. Первая часть находится по адресу https://github.com/aleshkashell/geekbrains_django

## Оглавление

- [Урок 1. Отправка электронной почты. Контекстные процессоры](#Урок-1)
- [Урок 2. Регистрация через социальную сеть. Django-ORM: связь один-к-одному](#Урок-2)

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

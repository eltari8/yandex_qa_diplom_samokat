# Тест на проверку того, что по треку заказа можно получить данные о заказе.
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск теста выполняется командой pytest

# РАБОТА С БАЗОЙ ДАННЫХ

## Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

*SELECT cour.login, COUNT(ord.track) FROM "Orders" AS ord INNER JOIN "Couriers" AS cour ON ord."courierId" = cour.id WHERE ord."inDelivery" = true GROUP by cour.login;*

## Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2. Если поле canсelled == true, то вывести статус -1. Если поле inDelivery == true, то вывести статус 1. Для остальных случаев вывести 0.

*SELECT track, CASE WHEN cancelled = true THEN -1 WHEN finished = true THEN 2 WHEN "inDelivery" = true THEN 1 ELSE 0 END From "Orders";*

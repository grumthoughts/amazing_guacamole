<<<<<<< HEAD
# Импортируем модуль data, который содержит данные для отправки в запросах, такие как заголовки и тело запроса
import data
# Импортируем модуль sender_stand_request, который содержит функции для отправки запросов и получения информации о заказе
import sender_stand_request

# Определение функции для тестирования успешного получения информации о заказе по его треку
def test_get_order_by_track_success():
    # Отправляем POST-запрос на создание нового заказа и получаем ответ
    creation_response = sender_stand_request.post_new_order(data.order_body)
    # Получаем трек заказа из ответа на POST-запрос
    track_id = creation_response.json()["track"]
    # Отправляем GET-запрос на получение информации о заказе по его треку и получаем ответ
    order_response = sender_stand_request.get_new_order(track_id)
    # Проверяем, что код ответа на GET-запрос равен 200, что означает успешное получение информации о заказе
    assert order_response.status_code == 200
=======
# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Функция для позитивной проверки
def positive_assert():
    # В переменную kits_body сохраняется обновлённое тело запроса
    response = sender_stand_request.get_new_order()
    # Проверяется, что код ответа равен 201
    assert response.status_code == 200
    

# Тест 1. Позитивная проверка
# Параметр name состоит из 2 символов
def test_create_order_success_response():
    positive_assert()
>>>>>>> ded9de0ea44b32734579eec9a78f464e919853ed

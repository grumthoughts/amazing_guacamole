<<<<<<< HEAD
# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration
# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests
# Импортируем модуль data, который содержит данные для отправки в запросах, такие как заголовки и тело запроса
import data

# Определение функции order_body для отправки POST-запроса на создание нового пользователя
def post_new_order(order_body):
    # Отправляем POST-запрос на URL, который состоит из базового URL и пути для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)

# Определение функции get_new_order для отправки GET-запроса на получение информации о заказе по его треку
def get_new_order(response_track):
    # Отправляем GET-запрос на URL, который состоит из базового URL и пути для получения заказа
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params={'t': response_track}, 
=======
# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

# Импортируем модуль data, который содержит данные для отправки в запросах, такие как заголовки и тело запроса
import data

# Определение функции order_body для отправки POST-запроса на создание нового пользователя
def post_new_order(order_body):
    # Отправляем POST-запрос на URL, который состоит из базового URL и пути для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)

# Определение функции get_new_order для отправки GET-запроса на получение информации о заказе по его треку
def get_new_order():
    # Получаем трек заказа из ответа на POST-запрос и используем его для отправки GET-запроса
    response = post_new_order(data.order_body).json()
    # Извлекаем значение трека из ответа на POST-запрос
    response_track = response["track"]
    # Отправляем GET-запрос на URL, который состоит из базового URL и пути для получения заказа
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params={'t': response_track}, 
>>>>>>> ded9de0ea44b32734579eec9a78f464e919853ed
                        headers=data.headers)
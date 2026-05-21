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

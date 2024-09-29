import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_items():
    print("1. Показать список товаров")
    print("2. Купить товар")
    print("3. Показать мой инвентарь")
    print("4. Заказать товар в магазин")
    print("5. Получить подробную информацию о товаре")


    print("6. Выход")

def hello_client():
    print("Здравствуй путник, хочу тебя поздравить, ты пришёл по адресу.")
    menu_items()
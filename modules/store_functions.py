from modules.hello_funcs import clear_console

def show_items(items):
    clear_console()
    print("=" * 100)
    for _, product in items.items():
        print(f"Имя товара: {product['name']}, Количество на складе 🏯: {product['count']}, Стоимость в рублях💵: {product['cost']}, Рейтинг⭐️: {product['rating']}/10")
    print("=" * 100)

    input("Продолжить...")

def buy_item(items, our_items, our_money):
    clear_console()
    print("Какой товар хотите купить?")
    for key, product in items.items():
        print(f"{key}. {product['name']}, Количество на складе 🏯: {product['count']}, Стоимость в рублях💵: {product['cost']}, Рейтинг⭐️: {product['rating']}/10")
    print(f"Счёт💵: {our_money}")
    keys_list = list(items.keys())
    choice = int(input("Я выбираю: "))
    selected_item = items[keys_list[choice]]

    if selected_item['cost'] > our_money:
        print("К сожалению у вас недостаточно средств🙁")
    else:
        selected_item['count'] -= 1
        our_money -= selected_item['cost']

        if selected_item['name'] in our_items:
            our_items[selected_item['name']] += 1
        else:
            our_items[selected_item['name']] = 1

        print(f"Вы купили товар {selected_item['name']}.")
        print(f"Остаток на счету💵: {our_money}")

        rate_item(selected_item)

def rate_item(selected_item):
    rating = int(input(f"Пожалуйста, оцените товар '{selected_item['name']}'"))

    if rating > 10 or rating < 0:
        print("Неверный рейтинг. Рейтинг должен быть от 0 до 10")
        return
    
    selected_item['rating'] = rating
    print(f"Спасибо за ваш рейтинг! Новый рейтинг для {selected_item['name']} : {selected_item['rating']}/10")

def add_item(items):
    clear_console()
    name = input("Введите имя товара: ")
    count = int(input("Введите количество товара: "))
    cost = int(input("Введите стоимость товара: "))
    description = input("Введите описание товара: ")

    elements = []

    comp_count = int(input("Введите количество элементов в составе товара: "))
    for _ in range(comp_count):
        element = input("Введите элемент в составе товара: ")
        elements.append(element)

    new_item_id = len(items)
    items[new_item_id] = {"name": name, "count": count, "cost": cost, "rating": 0, "product_composition": elements, "description": description}

    print(f"Товар {name} успешно заказан.")

def show_item(items):
    clear_console()
    for key, product in items.items():
        print(f"{key}. {product['name']}, Количество на складе 🏯: {product['count']}, Стоимость в рублях💵: {product['cost']}, Рейтинг⭐️: {product['rating']}/10")
    keys_list = list(items.keys())
    choice = int(input("Я выбираю: "))
    clear_console()
    selected_item = items[keys_list[choice]]
    print("=" * 100)
    print(selected_item['name'])
    print("_" * 100)
    print(selected_item['description'])
    print(f"Стоимость в рублях💵: {selected_item['cost']}")
    print(f"Количество на складе 🏯: {selected_item['count']}")
    print(f"Рейтинг⭐️: {selected_item['rating']}/10")
    print("_" * 100)
    print("Состав:")
    for element in selected_item['product_composition']:
        print("  - " + element)
    print("=" * 100)

    input("Продолжить...")
    

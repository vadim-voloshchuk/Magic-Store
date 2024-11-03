import json
import random
from modules.core.store_item import Item



class MagicStore:
    def __init__(self, name = "Полуночный Котел", store_size = 10000):
        self.name = name
        self.store_size = store_size
        self.current_size = 0
        self.items = []
    
    def load_items_from_file(self, items_path):
        with open(items_path, 'r', encoding='utf-8') as file:
            json_items = json.load(file)
        
        for i,item in json_items.items():
            current_item = Item(name = item['name'],
                                count=item['count'])

            #TODO: Добить здесь поля товара (говорить и писать что у меня лапки запрещено!!!!)
            
            print(f"В магический магазин {self.name} добавлен товар!")
            print(current_item)
            self.items.append(current_item)
        
    def generate_items(self):
        magic_items = [
            "Меч волшебства",
            "Щит заклинаний",
            "Жезл огненных шаров",
            "Кольцо защиты",
            "Амюлет силы",
            "Зелье исцеления",
            "Свиток света",
            "Книга заклинаний",
            "Ботинки магии",
            "Посох молнии",
            "Кристалл ясновидения",
            "Перо феникса",
            "Шкалька дракона",
            "Орт мифрила",
            "Арканный кристалл",
            "Книжка заклинаний",
            "Магическая перо",
            "Защищенное снаряжение",
            "Крылья ангела",
            "Стоящий стол"
        ]

        # Список возможных описаний
        descriptions = [
            "Необходим для защиты от злых духов.",
            "Позволяет летать над миром.",
            "Дает силу огня и света.",
            "Улучшает ловкость и скорость.",
            "Позволяет говорить с животными."
        ]

        magic_elements = ["Земля", "Вода", "Огонь", "Воздух", "Нет"]
        element_weights = [0.3, 0.25, 0.2, 0.15, 0.1]  # Вероятности выбора элементов

        count_items = random.randint(1, 15)

        for i in range(count_items):
            name = random.choice(magic_items)
            count = random.randint(1, 1000)
            cost = random.randint(1, 1000)
            elements = random.choices(magic_elements)
            description = random.choice(descriptions)

            new_item = Item(name = name, count=count, cost=cost, description=description, product_composition=elements)

            self.items.append(new_item)
            print(f"Товар {name} успешно заказан.")


    def show_items(self):
        print("=" * 100)
        for product in self.items:
            print(f"Имя товара: {product.get_name()}, Количество на складе 🏯: {product.get_count()}, Стоимость в рублях💵: {product.get_cost()}, Рейтинг⭐️: {product.get_rating()}/10")
        print("=" * 100)

    def show_item(self, name):
        find = True
        for item in self.items:
            if item.get_name() == name:
                print("=" * 100)
                print(item.get_name())
                print("_" * 100)
                print(item.get_description())
                print(f"Стоимость в рублях💵: {item.get_cost()}")
                print(f"Количество на складе 🏯: {item.get_count()}")
                print(f"Рейтинг⭐️: {item.get_rating()}/10")
                print("_" * 100)
                print("Состав:")
                for element in item.get_product_composition():
                    print("  - " + element)
                print("=" * 100)

                find = False
        if find:
            print(f"Товара, который вы указали не существует в магазине '{self.name}'.")
        

    def add_item(self, name, count, cost, description, elements):
        new_item = Item(name = name, count=count, cost=cost, description=description, product_composition=elements)

        self.items.append(new_item)
        print(f"Товар {name} успешно заказан.")

    def rate_item(self, name, value):
        find = True
        for item in self.items:
            if item.get_name() == name:
                item.set_rating(value)
                print(f"Спасибо за ваш рейтинг! Новый рейтинг для {item.get_name()} : {item.get_rating()}/10")
                find = False
        if find:
            print(f"Товара, который вы указали не существует в магазине '{self.name}'.")

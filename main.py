from common.pereferences import STORE_PATH, INVENTORY_PATH
from modules.work_with_files import load_inventory_from_txt, load_items_from_json
from modules.hello_funcs import clear_console

import json

class Item:
    def __init__(self, name = "Простой товар", count = 1, cost = 0, rating = 0, 
                product_composition = ["компонент 1", "компонент 2"],
                 description = "Условное описание"):
        
        self.name = name
        self.count = count
        self.cost = cost
        self.rating = rating
        self.product_composition = product_composition
        self.description = description
    
    def __str__(self):
        return f"Товар с названием: '{self.name}'"

    def get_description(self):
        return self.description
    
    def get_count(self):
        return self.count
    
    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name
    
    def get_rating(self):
        return self.rating

    def get_product_composition(self):
        return self.product_composition
    
    def get_description(self):
        return self.description

    def show_product_composition(self):
        print(f"Состав продукта: '{self.name}'")
        for pc in self.product_composition:
            print(pc)

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

    def show_items(self):
        print("=" * 100)
        for product in self.items:
            print(f"Имя товара: {product.get_name()}, Количество на складе 🏯: {product.get_count()}, Стоимость в рублях💵: {product.get_cost()}, Рейтинг⭐️: {product.get_rating()}/10")
        print("=" * 100)


ms1 = MagicStore()

ms1.load_items_from_file(STORE_PATH)

ms1.show_items()

#TODO: добавить в класс MagicStore методы add_item, show_item, rate_item

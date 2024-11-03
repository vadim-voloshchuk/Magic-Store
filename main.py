from common.pereferences import STORE_PATH, INVENTORY_PATH
from modules.work_with_files import load_inventory_from_txt, load_items_from_json
from modules.core.store_magicstore import MagicStore

class MainGame:
    def __init__(self, player_name = "Игрок 1"):
        self.player_name = player_name

        self.hello_player()

        while True:
            self.show_main_menu()

            choice = int(input("Я выбираю: "))

            if choice == 1:
                self.start_game()

            if choice == 3:
                break
        
        print("Спасибо за игру!")

    def show_main_menu(self):
        print("1. Начать новую игру")
        print("2. Продолжить")
        print("3. Выйти")
        
    def show_menu_items(self):
        print("1. Показать список товаров")
        print("2. Купить товар")
        print("3. Показать мой инвентарь")
        print("4. Заказать товар в магазин")
        print("5. Получить подробную информацию о товаре")

        print("6. Выход")

    def hello_player(self):
        print(f"Здравствуй {self.player_name}, хочу тебя поздравить, ты пришёл по адресу.")

    def start_game(self):
        self.my_ms = MagicStore()
        self.my_ms.generate_items()
        while True:
            self.show_menu_items()

            choice = int(input("Я выбираю: "))

            if choice == 1:
                self.my_ms.show_items()
            
            # if choice == 2:
            #     buy_item(items, our_items, our_money)
            
            # if choice == 3:
            #     show_inventory(our_items, our_money)
            
            if choice == 4:
                name = input("Введите имя товара: ")
                count = int(input("Введите количество товара: "))
                cost = int(input("Введите стоимость товара: "))
                description = input("Введите описание товара: ")

                elements = []

                comp_count = int(input("Введите количество элементов в составе товара: "))
                for _ in range(comp_count):
                    element = input("Введите элемент в составе товара: ")
                    elements.append(element)
                self.my_ms.add_item(name=name, cost=cost, count=count, description=description, elements=elements)
            
            if choice == 5:
                name = input("Введите имя товара: ")
                self.my_ms.show_item(name)
                
            if choice == 6:
                # save_items_to_json(STORE_PATH, items)
                # save_inventory_to_txt(INVENTORY_PATH, our_items, our_money)

                print("Спасибо, что посетили наш магазин! Возвращайтесь ещё!")
                break


game = MainGame()

# TODO: Сделать класс Invenory (ИГРОКА) и добавить его в игру :)
# Добавить в класс магазина метод buy_item, который будет покупать товар из магазина и добавлять в инвентарь :)
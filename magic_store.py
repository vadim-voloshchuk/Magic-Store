from common.pereferences import STORE_PATH, INVENTORY_PATH
from modules.work_with_files import load_inventory_from_txt, load_items_from_json, save_inventory_to_txt, save_items_to_json
from modules.store_functions import buy_item, show_items, add_item, show_item
from modules.inventory_funcs import show_inventory

from modules.hello_funcs import hello_client, clear_console


our_items, our_money = load_inventory_from_txt(INVENTORY_PATH)
items = load_items_from_json(STORE_PATH)

while True:
    clear_console()
    hello_client()
    
    choice = int(input("Я выбираю: "))

    if choice == 1:
        show_items(items)
    
    if choice == 2:
        # TODO: Расширить словарики товаров магазина добавив поле rating(от 0 до 10 число). Рейтинг товару можно дать после покупки.
        buy_item(items, our_items, our_money)
    
    if choice == 3:
        show_inventory(our_items, our_money)
    
    if choice == 4:
        add_item(items)
    
    if choice == 5:
        show_item(items)
        
    if choice == 6:
        save_items_to_json(STORE_PATH, items)
        save_inventory_to_txt(INVENTORY_PATH, our_items, our_money)

        print("Спасибо, что посетили наш магазин! Возвращайтесь ещё!")
        break


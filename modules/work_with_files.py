import json

# JSON - функции

def save_items_to_json(file_path, items):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=4)

def load_items_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# TXT - функции
def save_inventory_to_txt(file_path, inventory, money):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item_name, count in inventory.items():
            file.write(f"{item_name}: {count}\n")
        file.write(f"Остаток на счету: {money}")

def load_inventory_from_txt(file_path):
    inventory = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith("Остаток"):
                money_line = line.strip().split(":")
                return inventory, int(money_line[1])
            else:
                item_name, count = line.strip().split(":")
                inventory[item_name] = int(count)

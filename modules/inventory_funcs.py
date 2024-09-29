def show_inventory(our_items, our_money):
    print("=" * 100)
    for key, product in our_items.items():
        print(key, product)
    
    print(f"Счёт💵: {our_money}")
    print("=" * 100)

    input("Продолжить...")
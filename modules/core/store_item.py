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

    def set_rating(self, value):
        if value > 10 or value < 0:
            print("Неверный рейтинг. Рейтинг должен быть от 0 до 10")
            return
        self.rating = value

    def show_product_composition(self):
        print(f"Состав продукта: '{self.name}'")
        for pc in self.product_composition:
            print(pc)
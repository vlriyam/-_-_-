class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price} руб."

class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Товар '{product.name}' добавлен в заказ {self.order_number}")
    
    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def display_order(self):
        print(f"ЗАКАЗ №{self.order_number}")
        
        if not self.products:
            print("Заказ пуст")
        else:
            print("Товары в заказе:")
            for i, product in enumerate(self.products, 1):
                print(f"{i}. {product}")
        
        total = self.get_total_price()
        print(f"ИТОГО: {total} руб.")



product1 = Product("Клавиатура", 3000)
product2 = Product("Монитор", 25000)
product3 = Product("Мышь", 2300)
    
order1 = Order(1)
    
order1.add_product(product1)
order1.add_product(product3)

order1.display_order()

order2 = Order(2)
order2.add_product(product2)
order2.display_order()
    
print(f"\nОбщая стоимость заказа №1: {order1.get_total_price()} руб.")
print(f"Общая стоимость заказа №2: {order2.get_total_price()} руб.")
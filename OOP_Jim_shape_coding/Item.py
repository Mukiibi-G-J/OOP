class Item:
    def __init__(self, name):
        print(f"An instance crated:{name}")
        print("i am crated")

    def calculate_total_Price(self, x, y):
        return x*y


item1 = Item('laptop')
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_Price(item1.price, item1.quantity))

item2 = Item('phone')
item2.name = 'book'
item2.price = 1000
item2.quantity = 5

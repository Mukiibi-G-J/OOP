
class Item:

    def __init__(self, name, price, quantity=76, ):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_Price(self):
        return self.price*self.quantity


Item1 = Item("Laptop", 23)

print(Item1.name)
print(Item1.quantity)
# Not you can add more attubutes to an object
# Item1.has_num_pad = True

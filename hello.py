import csv
import os

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float ,quantity=0):
       # Run validations to the received arguments
       assert price >= 0, f"Price {price} is not greater or equal to zero!"
       assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

       # Assign to self object
       self.name = name
       self.price = price
       self.quantity = quantity

       # Actions to execute
       Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name=item['name'].strip(),
                price=float(item['price'].strip() or 0),
                quantity=int(item['quantity'].strip() or 0)
            )

        return cls.all
    
    @staticmethod
    def is_integer(num):
        # We will count decimals that are point zero
        # For i.e:5.0, 10.0
        if isinstance(num, (int, float)):
            return float(num).is_integer()
        return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


if __name__ == '__main__':
    Item.instantiate_from_csv()
    for item in Item.all:
        print(item)



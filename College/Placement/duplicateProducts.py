name = ["ball", "bat", "glove", "glove", "glove"]
price = [2, 3, 1, 2, 1]
weight = [2, 5, 1, 1, 1]

class Product:
    def __init__(self, name: str, price: int, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Weight: {self.weight}"

    def __eq__(self, other) -> bool:
        if self.name == other.name and self.weight == other.weight and self.price == other.price:
            return True
        else:
            return False

def duplicate_products(name, price, weight):
    products = []
    for i in zip(name, price, weight):
        temp = Product(i[0], i[1], i[2])
        if temp in products:
            print(temp)
            return
        else:
            products.append(temp)
    print("not found!")

duplicate_products(name, price, weight)

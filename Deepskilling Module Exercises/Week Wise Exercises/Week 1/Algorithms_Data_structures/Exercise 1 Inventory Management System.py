class Product:
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print("Product Added")

    def update_product(self, product_id, quantity, price):
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            self.products[product_id].price = price
            print("Product Updated")
        else:
            print("Product Not Found")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product Deleted")
        else:
            print("Product Not Found")

    def display(self):
        for p in self.products.values():
            print(p.product_id, p.product_name, p.quantity, p.price)


inv = Inventory()

inv.add_product(Product(101, "Laptop", 10, 50000))
inv.add_product(Product(102, "Mouse", 20, 500))

inv.display()

inv.update_product(101, 15, 52000)
inv.delete_product(102)

inv.display()
class Product:
    def __init__(self, product_id, product_name, category):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category

products = [
    Product(101, "Laptop", "Electronics"),
    Product(102, "Mobile", "Electronics"),
    Product(103, "Shoes", "Fashion")
]

def linear_search(products, key):
    for p in products:
        if p.product_name == key:
            return p
    return None

def binary_search(products, key):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2

        if products[mid].product_name == key:
            return products[mid]
        elif products[mid].product_name < key:
            low = mid + 1
        else:
            high = mid - 1

    return None

products.sort(key=lambda x: x.product_name)

result = linear_search(products, "Laptop")

if result:
    print("Found:", result.product_name)
else:
    print("Not Found")
class Order:
    def __init__(self, order_id, customer_name, total_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_price = total_price

orders = [
    Order(1, "Vaibhav", 2000),
    Order(2, "Rahul", 5000),
    Order(3, "Kiran", 3000)
]

def bubble_sort(orders):
    n = len(orders)

    for i in range(n):
        for j in range(0, n - i - 1):
            if orders[j].total_price > orders[j + 1].total_price:
                orders[j], orders[j + 1] = orders[j + 1], orders[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x.total_price <= pivot.total_price]
    right = [x for x in arr[1:] if x.total_price > pivot.total_price]

    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_orders = quick_sort(orders)

for order in sorted_orders:
    print(order.customer_name, order.total_price)
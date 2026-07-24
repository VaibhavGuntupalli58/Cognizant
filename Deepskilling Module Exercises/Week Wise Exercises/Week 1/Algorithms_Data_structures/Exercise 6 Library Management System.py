class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
books = [
    Book(1, "Python", "Guido"),
    Book(2, "Java", "James"),
    Book(3, "C Programming", "Dennis")
]
def linear_search(title):
    for book in books:
        if book.title == title:
            return book
    return None
def binary_search(title):
    books.sort(key=lambda x: x.title)
    low = 0
    high = len(books) - 1
    while low <= high:
        mid = (low + high) // 2
        if books[mid].title == title:
            return books[mid]
        elif books[mid].title < title:
            low = mid + 1
        else:
            high = mid - 1
    return None
book = linear_search("Python")
if book:
    print("Found:", book.title)
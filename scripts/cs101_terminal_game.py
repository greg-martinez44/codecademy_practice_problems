"""
A stupid little CLI game for Codecademy

Something like a text adventure... Maybe something really silly, like trying to
decide on a book in the book store?

"""

class Bookstore:
    CATEGORIES = [
        "Fantasy/Science Fiction",
        "Literature",
        "Young Adult",
        "Memoirs",
        "Science/Nature",
        "History",
        "New Bestsellers - Fiction",
        "New Bestsellers - Nonfiction"
        ]

    def __init__(self, name, size=10, inventory=None):
        self._name = name
        self._size = size
        self._inventory = inventory or []
        self._revenue = 0

    def __iter__(self):
        for book in self.inventory:
            yield book

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def inventory(self):
        return self._inventory

    @property
    def revenue(self):
        return self._revenue

    def add_to_inventory(self, book):
        self._inventory.append(book)

    def remove_book_from_inventory(self, book):
        if book not in self._inventory:
            raise ValueError("Book not in inventory")

        self._inventory.remove(book)

    def make_sale(self, name_of_book):
        book = self.find_book(name_of_book)
        self.remove_book_from_inventory(book)
        self._revenue += book.price

    def find_book(self, name_of_book):
        for book in self:
            if book.name == name_of_book:
                return book

    def print_inventory(self):
        return "\n".join([f"{book.name} by {book.author} for ${book.price}" for book in self])

class Book:

    def __init__(self, name, author, price):
        self._name = name
        self._author = author
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(new_price, (float, int)):
            raise TypeError("Price must be a number")

        self._price = new_price

INVENTORY = [
    Book("The Committed", "Viet Thanh Nguyen", 33),
    Book("A Programmer's Guide to Computer Science", "William Springer", 15.99),
    Book("The Name of the Wind", "Patrick Rothfuss", 29.99)
    ]

if __name__ == "__main__":
    new_store = Bookstore("My Store", inventory = INVENTORY)
    print(f"""
Welcome to {new_store.name}.
Our stock includes:
{new_store.print_inventory()}
    """)

    while True:
        user_choice = input("Which would you like to buy? ")
        if new_store.find_book(user_choice) is not None:
            break
        print("We do not have that in stock.")
    new_store.make_sale(user_choice)

    print(f"Thank you for you purchase. You've helped us raise ${new_store.revenue}")

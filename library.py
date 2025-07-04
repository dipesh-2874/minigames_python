class books:
    no_of_books = 0
    def __init__(self, name, author, pages):
        books.no_of_books += 1
        self.name = name
        self.author = author
        self.pages = pages

    def info(self):
        print(f"\nBook : {self.name} \nby {self.author} \ncontains {self.pages} pages.")

class premiumBooks(books):
    def __init__(self, name, author, pages, price):
        super().__init__(name, author, pages)
        self.price = price

    def info(self):
        super().info()
        print(f"This is a premium book. \nYou need to pay rupees {self.price} to access it.")

book1 = books('Barnaparichay', 'Iswar Chandra Vidyasagar',50)
book2 = premiumBooks('Rich dad Poor dad','Denis Richie', 300, 599)
book3 = books('Engineering Mathematics', 'Das & Pal', 650)

book1.info()
book2.info()
book3.info()

print(f"\nTotal number of books in the library : {books.no_of_books}")
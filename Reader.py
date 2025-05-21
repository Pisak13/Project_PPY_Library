class Reader:
    def __init__(self, id, firstname, lastname, address, phonenumber):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phonenumber = phonenumber
        self.borrowed_books = []




    def borrow(self, book):
            self.borrowed_books.append(book)

    def return_book(self, book):
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Reader(id: {self.id},firstname: {self.firstname},lastname: {self.lastname})"



from Book import Book
from Reader import Reader


class Library:
    def __init__(self):
        self.books = {},
        self.readers = {}

    def addBook(self, title, author, publisher, pages):
        isbn = max(self.books.keys(), default=0) + 1
        book = Book(isbn, title, author, publisher, pages)
        self.books[isbn] = book
        print(f"Book added: ISBN {isbn}")

    def deleteBook(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book {isbn} deleted.")
        else:
            raise Exception(f"Book {isbn} not found.")

    def updateBook(self, isbn, title=None, author=None, publisher=None, pages=None):
        if isbn not in self.books:
            raise Exception(f"Book {isbn} not found.")

        book = self.books[isbn]

        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if publisher is not None:
            book.publisher = publisher
        if pages is not None:
            book.pages = pages

        print(f"Book {isbn} updated.")

    def addReader(self, firstname, lastname, address, phonenumber):
        id = max(self.readers.keys(), default=0) + 1
        reader = Reader(id, firstname, lastname, address, phonenumber)
        self.readers[id] = reader
        print(f"Reader added: ID {id}")

    def deleteReader(self, id):
        if id in self.readers:
            del self.readers[id]
            print(f"Reader {id} deleted.")
        else:
            raise Exception(f"Reader {id} not found.")

    def updateReader(self, id, firstname=None, lastname=None, address=None, phonenumber=None):
        if id not in self.readers:
            raise Exception(f"Reader {id} not found.")

        reader = self.readers[id]

        if firstname is not None:
            reader.firstname = firstname
        if lastname is not None:
            reader.lastname = lastname
        if address is not None:
            reader.address = address
        if phonenumber is not None:
            reader.phonenumber = phonenumber

        print(f"Reader {id} updated.")

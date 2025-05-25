from warnings import catch_warnings

from Book import Book
from Reader import Reader
from datetime import date,timedelta


class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}

    def addBook(self, title, author, publisher, pages, isBorrowed=False) -> None:

        for isbn, copies in self.books.items():
            if copies and copies[0].title == title and copies[0].author == author:
                break
        else:
            isbn = max(self.books.keys(), default=0) + 1
            self.books[isbn] = []

        copy_id = len(self.books[isbn]) + 1
        book = Book(isbn, copy_id, title, author, publisher, pages)
        book.is_borrowed = isBorrowed
        self.books[isbn].append(book)
        print(f"Book added: ISBN {isbn}, copy_id {copy_id}")

    def deleteBook(self, isbn, copy_id) -> None:
        if isbn not in self.books:
            raise Exception(f"ISBN {isbn} not found.")

        for book in self.books[isbn]:
            if book.copy_id == copy_id:
                self.books[isbn].remove(book)
                print(f"Deleted Book: '{book.title}', copy_id {copy_id}")

                if not self.books[isbn]:
                    del self.books[isbn]
                return

        raise Exception(f"Copy ID {copy_id} not found for ISBN {isbn}.")

    def updateBook(self, isbn,  title=None, author=None, publisher=None, pages=None, is_borrowed=None) -> None:
        if isbn not in self.books:
            raise Exception(f"ISBN {isbn} not found.")

        for book in self.books[isbn]:

                if title is not None:
                    book.title = title
                if author is not None:
                    book.author = author
                if publisher is not None:
                    book.publisher = publisher
                if pages is not None:
                    book.pages = pages
                if is_borrowed is not None:
                    book.is_borrowed = is_borrowed
                print(f"Updated Book:{book.title}")
                return


    def addReader(self, firstname, lastname, address, phonenumber) -> None:
        id = max(self.readers.keys(), default=0) + 1
        numer = phonenumber
        isok = True
        while(isok==True):
            if(len(str(numer))!=9 ):
                numer = int(input("Niepoprawny podany numer telefonu. Podaj ponownie: "))
            else:
                isok = False

        reader = Reader(id, firstname, lastname, address, numer)
        self.readers[id] = reader
        print(f"Reader added: ID {id}")

    def deleteReader(self, id):
        if id in self.readers:
            del self.readers[id]
            print(f"Reader {id} deleted.")
        else:
            raise Exception(f"Reader {id} not found.")

    def updateReader(self, id, firstname=None, lastname=None, address=None, phonenumber=None) -> None:
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

    def borrowBook(self, copy_id, reader_id, isbn,borrow_days) -> None:

            if reader_id not in self.readers:
                raise Exception("Reader not found.")
            if isbn not in self.books:
                raise Exception("Book not found.")

            for key, values in self.books.get(isbn, [])[copy_id - 1].reservation.items():
                if(key <= date.today() <= values):
                    raise Exception(f"Book {isbn} already reserved for today.")

            for book in self.books[isbn]:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrow_date = date.today()
                    book.due_date = date.today() + timedelta(days=borrow_days)

                    self.readers[reader_id].borrow(book)

                    print(f"Reader {reader_id} borrowed book '{book.title}', copy_id {book.copy_id}")
                    print(f"Due date: {book.due_date}")
                    return

            raise Exception("No available copies of this book.")



    def returnBook(self, reader_id, isbn, copy_id) -> None:
        if reader_id not in self.readers:
            raise Exception("Reader not found.")
        if isbn not in self.books:
            raise Exception("Book not found.")

        reader = self.readers[reader_id]

        for book in reader.borrowed_books:
            if book.isbn == isbn and book.copy_id == copy_id:
                reader.return_book(book)
                book.is_borrowed = False

                today = date.today()
                if book.due_date and today > book.due_date:
                    days_overdue = (today - book.due_date).days
                    fee = days_overdue * 0.5
                    print(f"Book returned late! Overdue by {days_overdue} days. Fee: {fee:.2f} zł")
                else:
                    print(f"Book returned on time. No fee.")


                book.borrow_date = None
                book.due_date = None

                print(f"Reader {reader_id} returned book '{book.title}', copy_id {book.copy_id}")
                return

        raise Exception(f"Reader did not borrow book ISBN {isbn}, copy_id {copy_id}.")

    def listAllReaders(self) -> None:
        print("All readers:")
        found = False
        for key, value in self.readers.items():
            print(f"{key}: {value}")
            found = True
        if not found:
            print("No readers in database")

    def listAvailableBooks(self) -> None:
        print("Available books:")
        found = False
        for isbn, copies in self.books.items():
            for book in copies:
                if not book.is_borrowed:
                    print(f"- {book.title} (ISBN: {isbn}, copy_id: {book.copy_id})")
                    found = True
        if not found:
            print("No available books.")


    def listBorrowedBooks(self) -> None:
        print("Borrowed books:")
        found = False
        for isbn, copies in self.books.items():
            for book in copies:
                if book.is_borrowed:
                    print(f"- {book.title} (ISBN: {isbn}, copy_id: {book.copy_id}, due: {book.due_date})")
                    found = True
        if not found:
            print("No borrowed books.")












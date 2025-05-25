from datetime import date, timedelta
from Exceptions import ReaderNotFoundException,MaxExtendConflictException


class Reader:
    def __init__(self, id, firstname, lastname, address, phonenumber):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phonenumber = phonenumber
        self.borrowed_books = []
        self.history = []

    def saveOperation(self, title, operationType) -> None:
        self.history.append((date.today(), title, operationType))

    @staticmethod
    def showHistory(readerdict, readerid) -> None:
        if readerid not in readerdict:
            raise ReaderNotFoundException("Reader not found")
        reader = readerdict[readerid]
        print(f"History of reader {reader.id} {reader.firstname} {reader.lastname}:")
        if not reader.history:
            print("No history!")
            return
        for entry in reader.history:
            date, title, operationType = entry
            print(f" {date}: {operationType}, {title}")



    def extend(self, isbn,copyid, daysToExtend):
        if (daysToExtend > 7):
            raise MaxExtendConflictException("Days to extend cannot be greater than 7")
        for book in self.borrowed_books:
            if (book.copy_id == copyid and book.isbn == isbn):
                book.due_date = book.due_date + timedelta(days=daysToExtend)
                print(f"Book {book.title} due date time extended to {book.due_date}")
                self.saveOperation(book.title, "extended")


    def borrow(self, book) -> None:
        self.borrowed_books.append(book)
        self.saveOperation(book.title, "borrow")


    def return_book(self, book) -> None:
        self.borrowed_books.remove(book)
        self.saveOperation(book.title, "return")



    def __str__(self):
        return f"id: {self.id},{self.firstname}, {self.lastname}"




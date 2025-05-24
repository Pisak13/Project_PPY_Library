from datetime import datetime


class Book:
    def __init__(self, isbn, copy_id, title, author, publisher, pages):
        self.isbn = isbn
        self.copy_id = copy_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.is_borrowed = False
        self.borrow_date = None
        self.due_date = None
        self.reservation = {}


    def checkIfReservedOrBorrowed(self, startDate, endDate):
        if (self.borrow_date <= startDate <= self.due_date):
            raise Exception("Book cannot be reserved for the same date, when it is borrowed!")

        for key, value in self.reservation.items():
            if (key <= startDate <= value):
                raise Exception("Book is already reserved for this date!")

            if (key <= endDate <= value):
                raise Exception("Book is already reserved for this date!")

    def reserve(self, reservationStartDate, reservationDays) -> None:
        if reservationDays > 7:
            raise Exception("Book cannot be reserved for more than seven days")

        reservationDueDate = reservationStartDate + datetime.timedelta(days=reservationDays)

        self.checkIfReservedOrBorrowed(reservationStartDate, reservationDueDate)

        self.reservation[reservationStartDate] = reservationDueDate


    def __str__(self):
        return f"Book({self.title}, copy_id={self.copy_id}, borrowed={self.is_borrowed})"


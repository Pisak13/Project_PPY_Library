from Library import Library
from Reader import Reader
from Book import Book

library = Library()

print("Welcome to the library system. Select an option")
while True:
    print("1.Add Book")
    print("2.Update Book")
    print("3.Delete Book")
    print("4.AddReader")
    print("5.Update Reader")
    print("6.DeleteReader")
    print("7.Borrow Book")
    print("8.Return Book")
    print("9.List Available Books")
    print("10.List Borrowed Books")
    print("11.Show History")
    print("12.Extend Borrow")
    print("13.Reserve Book")
    print("14.List All Readers")
    print("15.Exit")
    option = int(input("Enter your choice: "))
    match option:
        case 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publisher = input("Enter book publisher: ")
            pages = int(input("Enter book pages: "))
            library.addBook(title, author, publisher, pages)
        case 2:
            isbn = int(input("Enter ISBN: "))
            title = input("Enter book title or skip: ")
            author = input("Enter book author or skip: ")
            publisher = input("Enter book publisher or skip: ")
            pages = input("Enter book pages: ")
            library.updateBook(isbn, title, author, publisher, pages)
        case 3:
            isbn = int(input("Enter ISBN: "))
            copy_id = int(input("Enter copy number: "))
            library.deleteBook(isbn, copy_id)
        case 4:
            firstname=input("Enter first name: ")
            lastname=input("Enter last name: ")
            address=input("Enter address: ")
            phonenumber=int(input("Enter phone number: "))
            library.addReader(firstname, lastname, address, phonenumber)
        case 5:
            id=int(input("Enter id reader: "))
            firstname=input("Enter first name or skip :")
            lastname=input("Enter last name or skip :")
            address=input("Enter address or skip :")
            phonenumber=int(input("Enter phone number: "))
            library.updateReader(id,firstname, lastname, address, phonenumber)
        case 6:
            id=int(input("Enter id: "))
            library.deleteReader(id)
        case 7:
            readerid=int(input("Enter reader id: "))
            isbn=int(input("Enter ISBN: "))
            days=int(input("Enter days: "))
            library.borrowBook(readerid, isbn, days)
        case 8:
            readerid=int(input("Enter reader id: "))
            isbn=int(input("Enter ISBN: "))
            copyid = int(input("Enter copy number: "))
            library.returnBook(readerid, isbn, copyid)
        case 9:
            library.listAvailableBooks()
        case 10:
            library.listBorrowedBooks()
        case 11:
            readerid=int(input("Enter reader id: "))
            Reader.showHistory(library.readers, readerid)
        case 12:
            copyid=int(input("Enter copy number: "))
            isbn=int(input("Enter ISBN: "))
            daysToExtend=int(input("Enter days to extend: "))
            for czytacz in library.readers.values():
                for ksiazki in czytacz.borrowed_books:
                    if copyid == ksiazki.copy_id and isbn==ksiazki.isbn:
                        reader = czytacz
            reader.extend(copyid, daysToExtend)
        case 13:
            Book.reserve()
        case 14:
            library.listAllReaders()
        case 15:
            print("Goodbye")
            break
        case default:
            print("Sorry, I don't understand that. Please try again.")

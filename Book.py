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

    def __str__(self):
        return f"Book({self.title}, copy_id={self.copy_id}, borrowed={self.is_borrowed})"


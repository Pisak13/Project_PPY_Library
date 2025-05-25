class Exceptions(Exception):
    pass


class BookNotFoundException(Exceptions):
    pass
class ReaderNotFoundException(Exceptions):
    pass
class BookAlreadyReservedException(Exceptions):
    pass
class BookCopyNotFoundException(Exceptions):
    pass
class BookStillBorrowedException(Exceptions):
    pass
class BookReservationConflictException(Exceptions):
    pass
class IsbnNotFoundException(Exceptions):
    pass
class NoAvailableCopyBookException(Exceptions):
    pass
class ReturnException(Exceptions):
    pass
class MaxExtendConflictException(Exceptions):
    pass
class MaxRservationDaysExceededException(Exceptions):
    pass

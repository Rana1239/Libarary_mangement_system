class Book:
    def __init__(self,book_title,book_author,book_gener,book_loc,book_status=True,book_id=None):
        self.book_id=book_id
        self.book_title=book_title
        self.book_author=book_author
        self.book_gener=book_gener
        self.book_status=book_status
        self.book_loc=book_loc
        
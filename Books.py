def create_book( book_title, book_author, book_gener, book_loc, book_status=True, book_id=None):
    return {
        'book_id': book_id,
        'book_title': book_title,
        'book_author': book_author,
        'book_gener': book_gener,
        'book_loc': book_loc,
        'book_status': book_status
    }

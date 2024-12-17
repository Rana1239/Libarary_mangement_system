from datetime import datetime
import time
from Books import *
import pyodbc
def create_connection():
    conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};' \
        r'SERVER=localhost\SQLEXPRESS;' \
        r'DATABASE=libraryDB2;' \
        r'Trusted_Connection=yes;'
        
    conn = pyodbc.connect(conn_str)
    return conn

conn=create_connection()
cursor=conn.cursor()

def check_book_id(book_id):
       
    cursor.execute('SELECT 1 FROM BOOKS WHERE bookID=?',book_id)
    res=cursor.fetchone()
                        
    if res:
        return True
    return False
        
def save_book(book_obj):
    
    book_data=(book_obj['book_title'],book_obj['book_author'],book_obj['book_gener'],book_obj['book_loc'],True)
    cursor.execute('''
                        INSERT INTO Books (Title,Author,Genre,Location,Available)
                        VALUES (?,?,?,?,?)
                        ''',book_data)
    conn.commit()
    
    
def db_update_book(book_obj):
    book_data=(book_obj['book_title'],book_obj['book_author'],book_obj['book_gener'],book_obj['book_loc'],True,book_obj.book_id)
    cursor.execute('''
                        UPDATE Books 
                        SET Title=?,Author=?,Genre=?,Location=?,Available=?
                        Where bookID=?
                        ''',book_data)
    conn.commit()
    return True


def db_remove_book(book_id):
    cursor.execute('SELECT bookID, Title, Author, Genre, Location, Available FROM Books WHERE bookID = ?', (book_id,))
    book_row = cursor.fetchone()

    if book_row:  
        cursor.execute('DELETE FROM Books WHERE bookID = ?', (book_id,))
        conn.commit()
    return True
        

def db_view_members():
    try:
        cursor.execute('SELECT MemberID, Name, Phone FROM Members')
        rows = cursor.fetchall()

        for row in rows:
            print("ID:", row[0], end=" ")
            print("Name:", row[1], end=" ")
            print("Number:", row[2])
            print('-' * 43)
            time.sleep(1)
        conn.close()
        
    except Exception as e:
        print("Error retrieving members:", e)
    
    
def check_mem_id(id):
    cursor.execute('SELECT 1 FROM MEMBERS WHERE MemberID=?',id)
    res=cursor.fetchone()
                        
    if res:
        return True
    return False

def save_member(mem_obj):
    member_data=(mem_obj['member_name'],mem_obj['member_number'])
    cursor.execute('''
                        INSERT INTO Members (Name,Phone)
                        VALUES (?,?)
                        ''',member_data)
    conn.commit()
        
def db_update_member(mem_obj):
    member_data=(mem_obj['member_name'],mem_obj['member_number'],mem_obj['member_id'])
    cursor.execute('''
                        UPDATE Members
                        SET Name=?,Phone=?
                        Where MemberID=?
                        ''',member_data)
    conn.commit()
    return True

def db_borrow_book(mem_id, book_id):
    try:
        cursor.execute('SELECT Available FROM Books WHERE bookID = ?', (book_id,))
        result = cursor.fetchone()

        if not result[0]: 
            print("Book is already borrowed.")
            return False

        cursor.execute('''
        UPDATE Books 
        SET Available = 0 
        WHERE bookID = ?''', (book_id,))
    
        cursor.execute('''
        INSERT INTO Transactions (BookID, MemberID, BorrowDate)
        VALUES (?, ?, GETDATE())
        ''', (int(book_id), int(mem_id)))

        conn.commit()
        print("Book borrowed successfully.")
        return True

    except Exception as e:
        print("Error borrowing the book:", e)
        conn.rollback()
        return False


def db_return_book(mem_id, book_id):
    
    try:
        cursor.execute('SELECT Available FROM Books WHERE bookID = ?', (book_id,))
        result = cursor.fetchone()

        if result and result[0]: 
            print("Book is already available.")
            return False

        cursor.execute('SELECT BorrowDate FROM Transactions WHERE BookID = ? AND MemberID = ? AND ReturnDate IS NULL', (book_id, mem_id))
        borrow_result = cursor.fetchone()

        if borrow_result is None:
            print("No active borrowing record found for this book and member.")
            return False

        borrow_date = borrow_result[0]
        current_date = datetime.now()

        borrow_date = datetime.combine(borrow_date, datetime.min.time())
        
        late_days = (current_date - borrow_date).days
        fine_amount = 0

        if late_days > 10:
            fine_amount = (late_days - 10) * 5

        cursor.execute('''
        UPDATE Transactions
        SET ReturnDate = GETDATE(), FineAmount = ?
        WHERE BookID = ? AND MemberID = ? AND ReturnDate IS NULL
        ''', (fine_amount, int(book_id), int(mem_id)))

        cursor.execute('''
        UPDATE Books
        SET Available = 1
        WHERE bookID = ?
        ''', (book_id,))
    
        conn.commit()

        if fine_amount > 0:
            print(f"Book returned with a fine of {fine_amount} units.")
        else:
            print("Book returned successfully with no fine.")

        return True

    except Exception as e:
        print(f"Error returning the book: {e}")
        conn.rollback()
        return False
    

def get_all_avaliable_books():
    try:
        cursor.execute('''
        SELECT bookID, Title, Author, Genre, Location 
        FROM Books
        WHERE Available = 1
        ''')
    
        rows = cursor.fetchall()
        if not rows:
            print("No available books")
            return
        
        
        print("Available Books:\n")
        for row in rows:
            print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Gener: {row[3]}, Location: {row[4]}")

    except Exception as e:
        print(f"Error retrieving available books: {e}")
        return []
    
def db_history_of_borrowings(mem_id):
    
    cursor.execute('''
    SELECT t.BookID, t.BorrowDate, t.ReturnDate, t.FineAmount
    FROM Transactions t
    JOIN Books b ON t.BookID = b.BookID
    WHERE t.MemberID = ?
    ORDER BY t.BorrowDate DESC
    ''', (mem_id,))

    rows = cursor.fetchall()

    if rows:
        print(f"Borrowing history for Member ID {mem_id}:")
        for row in rows:
            print(f"Book ID: {row[0]}, Borrowed on: {row[1]}, Returned on: {row[2]}, Fine Amount: {row[3]}")
    
    else:
        print(f"No borrowing history found for Member ID {mem_id}.")

time.sleep(1)

def display_records():
    try:
        
        cursor.execute('''
        SELECT TransactionID, BookID, MemberID, BorrowDate, ReturnDate, FineAmount
        FROM Transactions
        ''')
    
        rows = cursor.fetchall()
        if not rows:
            print("No available transactions")
            return
        
        
        print("Transactions:")
        for row in rows:
            print(f"Transaction ID: {row[0]}, Book ID: {row[1]}, Member ID: {row[2]}, Borrow Date: {row[3]}, Return Date: {row[4]}, Fine Amount: {row[5]}\n")

    except Exception as e:
        print(f"Error retrieving books transactions: {e}")
        return []

def check(index,element):
    
    if index==1:
        cursor.execute('''
        SELECT bookID, Title, Author, Genre, Location
        FROM Books
        WHERE Title LIKE ?
        ''', ('%' + element + '%',))  # Using LIKE to match the title with partial text

        rows = cursor.fetchall()

        if rows:
            search(rows)
            return True
        
    if index==2:
        cursor.execute('''
        SELECT bookID, Title, Author, Genre, Location
        FROM Books
        WHERE Author LIKE ?
        ''', ('%' + element + '%',))  # Using LIKE to match the author with partial text
    
        rows = cursor.fetchall()

        if rows:
            search(rows)
            return  True
        
    if index==3:

        cursor.execute('''
        SELECT bookID, Title, Author, Genre, Location
        FROM Books
        WHERE Genre LIKE ?
        ''', ('%' + element + '%',))  # Using LIKE to match the genre with partial text
    
        rows = cursor.fetchall()

        if rows:
            search(rows)
            return True
    return False
    

def search(rows):
    for row in rows:
        print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Location: {row[4]}\n")
        return True
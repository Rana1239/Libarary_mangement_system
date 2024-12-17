import time
from Books import create_book
from member import create_member
from database import *

def add_book():
    book_title = input("Enter book name\n")
    book_author = input("Enter book author\n")
    book_gener = input("Enter book gener\n")
    book_loc = input("Enter book location\n")
    book_obj = create_book( book_title, book_author, book_gener, book_loc)
    save_book(book_obj)
    print("Book saved.")
    time.sleep(1)
    

def update_book():
    book_id = input("Enter book id\n")
    selected_book_id = check_book_id(book_id)
    
    if selected_book_id:
        book_title = input("Enter the updated book title\n")
        book_author = input("Enter the updated book author\n")
        book_gener = input("Enter the updated book gener\n")
        book_loc = input("Enter the updated book location\n")
        book_obj = create_book(book_id, book_title, book_author, book_gener, book_loc)
        
        if db_update_book(book_id,book_obj):
            print("Book updated")
        else:
            print("Error")
    else:
        print("Wrong id.")
        time.sleep(1)
        

def remove_book():
    book_id=input("Enter the book id to remove\n")
    selected_book_id=check_book_id(book_id)
    if selected_book_id:
        if  db_remove_book(book_id):
            print("Book deleted")
    else:
        print("Error: check book id\n")
        time.sleep(1)


def register_member():
    member_name = input("Enter member name\n")
    member_number = input("Enter member number\n")
    mem_obj = create_member( member_name, member_number)
    save_member(mem_obj)
    print("Member added.")
    time.sleep(1)

def view_members():
    db_view_members()

def update_member_det():
    mem_id = input('Enter member id to update\n')
    selected_mem_id = check_mem_id(mem_id)
    
    if selected_mem_id:
        member_name = input("Enter the updated member name\n")
        member_number = input("Enter the updated member number\n")
        mem_obj = create_member(mem_id, member_name, member_number)
        
        if db_update_member(mem_id,mem_obj):
            print("Member details updated")
        else:
            print("Error")
    else:
        print("Wrong id.")
    time.sleep(1)


def borrow_book():
    member_id = input("Enter your id\n")
    
    if not check_mem_id(member_id):
        print("Your id is wrong.")
    else:
        book_id = input("Enter the book id\n")
        if not check_book_id(book_id):
            print("Wrong book id.")
        else:
            db_borrow_book(member_id, book_id)
    time.sleep(1)


def return_book():
    member_id = input("Enter your id\n")
    
    if not check_mem_id(member_id):
        print("Your id is wrong.")
    else:
        book_id = input("Enter the book id\n")
        if not check_book_id(book_id):
            print("Wrong book id.")
        else:
            if db_return_book(member_id, book_id):
                print("Done")
            else:
                print("Error")
    time.sleep(1)


def view_records():
    display_records()

def get_available_books():
    return get_all_avaliable_books()

def history_of_borrowings():
    member_id=input("Enter your id\n")
    if not (check_mem_id(member_id)):
        print("Error, check your id.")
            
    else:
        return db_history_of_borrowings(member_id)

def search_title():
    title = input("Enter book title\n")
    selected_book_title = check(1,title)
    
    if selected_book_title:
        search(1,title)
    else:
        print("Unmatched title.")
        time.sleep(1)

def search_author():
    author = input("Enter book author\n")
    selected_book_author = check(2,author)
    
    if selected_book_author:
        search(2,author)
    else:
        print("Unmatched author.")
        time.sleep(1)

        
def search_gener():
    gener = input("Enter book author\n")
    selected_book_gener = check(3,gener)
    
    if selected_book_gener:
        search(3,gener)
    else:
        print("Unmatched gener.")
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
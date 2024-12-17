import os
import time
from Books import *
from mangement import *
from member import *
def clear_screen():
    os.system("cls" if(os.name=="nt") else "clear")
def book_mang():
    options=[1,2,3,4]
    print('-------------------------------------------')
    print('|              Book Mangement             |')
    print('-------------------------------------------')
    print('|          1. Add Book                    |')
    print('|          2. Remove Book                 |')
    print('|          3. Update Book                 |')
    print('|          4. Search                      |')
    print('-------------------------------------------')
    choice = int(input('Enter your option\n'))
    book_mang=Mangement()
    if choice in options:
        match choice:
            case 1:
                book_mang.add_books()
            case 2:
                book_mang.remove_book()
            case 3:
                book_mang.update_books()  
            case 4:
                search()              
    else:
        print("Invalid option")

    return 0
def member_mang():
    options=[1,2,3]
    print('-------------------------------------------')
    print('|            Member Mangement             |')
    print('-------------------------------------------')
    print('|          1. Register new members        |')
    print('|          2. View members                |')
    print('|          3. Update member details       |')
    print('-------------------------------------------')
    choice = int(input('Enter your option\n'))
    member_mang=Mangement()
    if choice in options:
        match choice:
            case 1:
                member_mang.register_member()
            case 2:
                member_mang.view_members()
            case 3:
                member_mang.update_member_det()
    else:
        print("Invalid option")

def borrowing_returning():
    options=[1,2,3]
    print('-------------------------------------------')
    print('|             Borrow&Return               |')
    print('-------------------------------------------')
    print('|          1. Borrow a book               |')
    print('|          2. Return a book               |')
    print('|          3. View book records           |')
    print('-------------------------------------------')
    choice = int(input('Enter your option\n'))
    borrow_return=Mangement()
    if choice in options:
        match choice:
            case 1:
                borrow_return.borrow_book()
            case 2:
                borrow_return.return_book()
            case 3:
                borrow_return.view_records()
    else:
        print("Invalid option")
def search():
    options=[1,2,3,4]
    print('-------------------------------------------')
    print('|              Search by                  |')
    print('-------------------------------------------')
    print('|          1. Title                       |')
    print('|          2. Author                      |')
    print('|          3. Gener                       |')
    print('-------------------------------------------')
    choice = int(input('Enter your option\n'))
    search=Mangement()
    if choice in options:
        match choice:
            case 1:
                search.search_title()
            case 2:
                search.search_author()
            case 3:                    
                search.search_gener()
    else:
        print("Invalid option")
        
def reports():
    print('-------------------------------------------')
    print('|   1. Available Books                    |')
    print('|   2. History of borrowings by a member  |')
    print('-------------------------------------------')
    options=[1,2]
    choice = int(input('Enter your option\n'))
    reports=Mangement()
    if choice in options:
        match choice:
            case 1:
                reports.get_available_books()
            case 2:
                reports.history_of_borrowings()
    else:
        print("Invalid option")
        
        
def main_interface():
    options=[1,2,3,4]
    while True:
        print('-------------------------------------------')
        print('|                  Home                   |')
        print('-------------------------------------------')
        print('|          1. Book Mangement              |')
        print('|          2. Member Mangement            |')
        print('|          3. Borrowing & Returning       |')
        print('|          4. Reports                     |')
        print('|          5. Exit                        |')
        print('-------------------------------------------')
        choice = int(input('Enter your option\n'))
        
        if choice in options:
            match choice:
                case 1:
                    book_mang()
                case 2: 
                    member_mang()
                case 3: 
                    borrowing_returning()   
                case 4:
                    reports()     
                case 5:
                    print("Exiting the system...")
                    time.sleep(1)
                    break
        else:
            print("Invalid option, please enetr a valid choice")   
            time.sleep(1)    
main_interface()
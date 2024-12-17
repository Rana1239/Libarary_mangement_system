from Books import *
from mangement import *
from member import *


def book_menu(): 
    menu=(
    '------------------------------------------\n'
    '|              Book Management           |\n' 
    '------------------------------------------\n' 
    '|          1. Add Book                   |\n' 
    '|          2. Remove Book                |\n' 
    '|          3. Update Book                |\n' 
    '|          4. Search                     |\n' 
    '------------------------------------------\n' 
    )
    print(menu)
    return(int(input('Enter your option\n')))
    

def book_mang():
    menu_options={
        1 : add_book,
        2 : remove_book,
        3 : update_book,
        4 : search
    }
    
    choice=book_menu()
    return menu_options.get(choice,invalid_option)()


def member_menu(): 
    menu=(
    '-------------------------------------------\n'
    '|            Member Management            |\n' 
    '-------------------------------------------\n' 
    '|          1. Register new member         |\n' 
    '|          2. View members                |\n' 
    '|          3. Update member details       |\n' 
    '-------------------------------------------\n' 
    )
    print(menu)
    return(int(input('Enter your option\n')))
 
def member_mang():
    menu_options={
        1 : register_member,
        2 : view_members,
        3 : update_member_det,
    }
    choice=member_menu()
    return menu_options.get(choice,invalid_option)()


def borrow_return_menu():
    menu=(
    '-------------------------------------------\n' 
    '|             Borrow & Return             |\n' 
    '-------------------------------------------\n' 
    '|          1. Borrow a book               |\n' 
    '|          2. Return a book               |\n' 
    '|          3. View book records           |\n' 
    '-------------------------------------------\n' 
    )
    print(menu)
    return(int(input('Enter your option\n')))

def borrowing_returning():
    menu_options={
        1 : borrow_book,
        2 : return_book,
        3 : view_records,
    }
    choice=borrow_return_menu()
    return menu_options.get(choice,invalid_option)()

def search_menu():
    menu=(
    '-------------------------------------------\n' 
    '|              Search by                  |\n' 
    '-------------------------------------------\n' 
    '|          1. Title                       |\n' 
    '|          2. Author                      |\n' 
    '|          3. Genre                       |\n' 
    '-------------------------------------------\n' 
    )
    print(menu)
    return(int(input('Enter your option\n')))

def search():
    menu_options={
        1 : search_title,
        2 : search_author,
        3 : search_gener,
    }
    choice=search_menu()
    return menu_options.get(choice,invalid_option)()

def reports_menu():
    menu=(
    '-------------------------------------------\n'
    '|   1. Available Books                    |\n'
    '|   2. History of borrowings by a member  |\n'
    '-------------------------------------------\n'
    )
    print(menu)
    return(int(input('Enter your option\n')))

def reports():
    menu_options={
        1 : get_available_books,
        2 : history_of_borrowings,
    }
    choice=reports_menu()
    return menu_options.get(choice,invalid_option)()

def exit_system():
    print("Exiting the system...")
    return False

def invalid_option():
    print("Invalid option, please enter a valid choice")


def format_menu(menu_options,result=""):
    if not menu_options:
        return result
    key, value=menu_options[0]
    result +=f"{key}. {value}\n"
    return format_menu(menu_options[1:],result)

def display_menu(menu_options):
    
    menu_text=format_menu(menu_options)  
    print(menu_text)      
    user_input=(int(input('Enter your option\n')))
    
    return user_input


menu_options=(
        (1 , "Book Mangement"),
        (2 , "Member Mangement"),
        (3 , "Borrowing & Returning"),
        (4 , "Reports"),
        (5 , "Exit")
    )    

def get_action(option,menu_actions):
    if not menu_actions:
        return None
    
    key,action= menu_actions[0]
    if key==option:
        return action
    return get_action(option, menu_actions[1:])

def main_interface(menu_options):
    menu_actions=(
        (1 , book_mang),
        (2 , member_mang),
        (3 , borrowing_returning),
        (4 , reports),
        (5 , exit_system)
    ) 
    
    def loop():
        option=display_menu(menu_options)
        action=get_action(option,menu_actions)
        if action is None:
            invalid_option()
            return loop()
        
        if action() is False:
            return 
        return loop()
    return loop()

         
main_interface(menu_options)

















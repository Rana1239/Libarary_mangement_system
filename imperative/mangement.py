from Books import Book
from member import Member
from database import Database
import time
class Mangement:
    db=Database()
    def __int__(self):
        pass
    def add_books(self):
        book_title=input("Enter book name\n")
        book_author=input("Enter book author\n")
        book_gener=input("Enter book gener\n")
        book_loc=input("Enter book location\n")
        book_obj=Book(book_title,book_author,book_gener,book_loc)
        self.db.save_book(book_obj)
        print("Book saved.")
        time.sleep(1)
        
        
    def update_books(self):
        book_id=input("Enter book id\n")
        selected_book_id=self.db.check_book_id(book_id)
        if selected_book_id:
            book_author=input("Enter the updated book author\n")
            book_title=input("Enter the updated book title\n")
            book_gener=input("Enter the updated book gener\n")
            book_loc=input("Enter the updated book location\n")
            book_obj=Book(book_title,book_author,book_gener,book_loc,1,book_id)
            if self.db.update_book(book_obj):
                print("Book updated")
            else:
                print("Error")
        else:       
            print("Wrong id.")
            time.sleep(1)
            
            
    def remove_book(self):
        book_id=input("Enter the book id to remove\n")
        selected_book_id=self.db.check_book_id(book_id)
        if selected_book_id:
                if  self.db.remove_book(book_id):
                    print("Book deleted")
        else:
            print("Error: check book id\n")
        time.sleep(1)
        
        
    def register_member(self):
        member_name=input("Enter member name\n")
        member_number=input("Enter member number\n")
        mem_obj=Member(member_name,member_number)
        self.db.save_member(mem_obj)
        print("Member added.")
        time.sleep(1)
        
        
    def view_members(self):
        self.db.view_members()
        
        
    def update_member_det(self):
        mem_id=input('Enter member id to update\n')
        selected_mem_id=self.db.check_mem_id(mem_id)
        if selected_mem_id:
            member_name=input("Enter the updated member name\n")
            member_number=input("Enter the updated member number\n")
            mem_obj=Member(mem_id,member_name,member_number)
            if self.db.update_mem(mem_obj):
                print("Member details updated")
            else:
                print("Error")
        else:
            print("Wrong id.")
        time.sleep(1)
        
        
    def borrow_book(self):
        member_id=input("Enter your id\n")
        if not (self.db.check_mem_id(member_id)):
            print("your id is wrong.")
        else:
            book_id=input("Enter the book id\n")
            if not(self.db.check_book_id(book_id)):
                print("Wrong book id.")
            else:
                if self.db.borrow_book(member_id,book_id):
                    print("Done")
                else:
                    print("Error")
        time.sleep(1)
    
    
    def return_book(self):
        member_id=input("Enter your id\n")
        if not (self.db.check_mem_id(member_id)):
            print("your id is wrong.")
        else:
            book_id=input("Enter the book id\n")
            if not(self.db.check_book_id(book_id)):
                print("Wrong book id.")
            else:
                self.db.return_book(member_id,book_id):
        time.sleep(1)
        
        
    def get_available_books(self):
        return self.db.get_all_avaliable_books()
    
    def history_of_borrowings(self):
        member_id=input("Enter your id\n")
        if not (self.db.check_mem_id(member_id)):
            print("Error, check your id.")
            
        else:
            return self.db.history_of_borrowings(member_id)
        
        
    def view_records(self):
        self.db.display_records()
        
        
    def search_title(self):
        title=input("Enter book title\n")
        selected_book_title=self.db.check(1,title)
        if not selected_book_title:      
            print("Unmatched title.")
            time.sleep(1)
        
            
    def search_author(self):
        author=input("Enter book author\n")
        selected_book_author=self.db.check(2,author)
        if not selected_book_author:       
            print("Unmatched author.")
            time.sleep(1)
        
            
    def search_gener(self):
        gener=input("Enter book gener\n")
        selected_book_gener=self.db.check(3,gener)
        if not selected_book_gener:      
            print("Unmatched gener.")
            time.sleep(1)
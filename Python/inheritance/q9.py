'''
Library Management

Parent:

LibraryItem

Derived:

Book
Magazine
Newspaper

Implement borrowing system.
'''
from abc import ABC, abstractmethod
class LibraryItem:
    def __init__(self, name):
        self.__name=name
        self.isavailable=True
        
    def get_name(self):
        return self.__name
    
    @abstractmethod
    def issue(self):
        pass
    
    @abstractmethod
    def returning(self):
        pass
    
class Book(LibraryItem):
    def issue(self):
        if self.isavailable==True:
            self.isavailable=False
            print("Book issued Successfully")
        else:
            print("Book is Not available")
            
    def returning(self):
        if self.isavailable==False:
            self.isavailable=True
            print("Book Returned Successfully")
        else:
            print("Book is Already here")
            
class Magazing(LibraryItem):
    def issue(self):
        if self.isavailable==True:
            self.isavailable=False
            print("Magazing issued Successfully")
        else:
            print("Magazing is Not available")
            
    def returning(self):
        if self.isavailable==False:
            self.isavailable=True
            print("Magazing Returned Successfully")
        else:
            print("Magazing is Already here")
            
class Newspaper(LibraryItem):
    def issue(self):
        if self.isavailable==True:
            self.isavailable=False
            print("Newspaper issued Successfully")
        else:
            print("newspaper is Not available")
            
    def returning(self):
        if self.isavailable==False:
            self.isavailable=True
            print("Newspaper Returned Successfully")
        else:
            print("Newspaper is Already here")
            
            
B1=Book("chhava")
B1.issue()
B1.issue()
B1.returning()

M1=Magazing("Naruto")
M1.issue()
M1.returning()

N1=Newspaper("Agnibann")
N1.issue()
N1.returning()
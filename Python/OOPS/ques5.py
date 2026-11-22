class Book:
    def __init__(self,id,title,author):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__status = True  
    
    def issue(self):
        if self.is_available():
            print(f"Book issued...")
            self.__status = False
        else:
            print(f"Book not available...")        
    
    def is_available(self):
        return self.__status

    def submit(self):
        if not self.is_available():
            self.__status = True
            print(f"Book Returned..")
        else:
            print(f"Book not issued")     

b1 = Book(100,"Java","Patrik norton")
print(f"{"Book Available" if b1.is_available() else "Not Avaialble"}")
b1.issue()
b1.submit()            
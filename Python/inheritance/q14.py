'''14. Multiple Inheritance Example

Classes:

Father
Mother
Child(Father, Mother)

Access methods from both.
'''

class Father:
    def eye(self):
        print("Father Eye")

class Mother:

    def face(self):
       print("Mother Face")
    
    
class Child(Father,Mother):
    
    def display(self):
        self.eye()
        self.face()


c1 = Child()
c1.display()
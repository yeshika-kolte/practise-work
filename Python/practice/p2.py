class A:
    def __init__(self):
        print("gm...")

    def wish(self):
        print("good morning")

    @classmethod
    def m1(cls):
        print("m1 class method")

    def m2(self):
        print("m2 instance method")


class B(A):
    def __init__(self):
        super().__init__()   
        super().wish()       
        super().m1()         
        super().m2()         

    @classmethod
    def m1(cls):
        super(B, cls).m1()   
        obj = cls()
        obj.m2()
    @staticmethod
    def m2():
        super(B, B).m2()
        

b = B()

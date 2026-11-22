class A:
    def __init__(self):
        print("A class constructor")

    def m1(self):
        print("M1 called")
    
    @classmethod
    def m2(cls):
        print("M2 Class method executed...")

    @staticmethod
    def m3():
        print("M3 static method executed...")

class B(A):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def inst_method(self):
        print("Instance Method")
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def class_method(cls):
        print("Class Method")
        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)
        super().m2()
        super().m3()

    @staticmethod
    def static_method():
        print("Static Method")
        super(B,B).m3()
        super(B,B).m1(B)

obj = B()
obj.inst_method()
obj.class_method()
obj.static_method()
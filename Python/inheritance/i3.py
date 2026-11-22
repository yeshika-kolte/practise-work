class A:
    error1 = 200
    def __init__(self):
        self.error2 = 404


class B(A):
    def displayError(self):
        print(self.error1)
        print(self.error2)
        print(super().error1)
        # print(super().error2) show error


obj = B()
obj.displayError()
#Structural Pattern

class Decorator:
    def test(self):
        print("Class method")

    @staticmethod
    def static_test():
        print("Static method")

x=Decorator()
x.test()
#  x.static_test()

#  Decorator.test()
Decorator.static_test()

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # Diamond inheritance
    pass

# Creating an instance of D
d = D()
d.greet()

# Checking the MRO
print(D.mro())
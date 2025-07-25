print(hash("hello"))  
print(hash(42))       
print(hash((1, 2, 3))) 
try:
    print(hash([1, 2, 3])) 
except TypeError as e:
    print(e)

class MyClass:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

obj = MyClass(10)
print(hash(obj))  



def fibonacciTable(n): 
    a = 0
    b = 1
    if (n >= 0): 
        print(a) 
    if (n >= 1): 
        print(b) 
    for i in range(2, n+1): 
        c = a + b 
        print(c) 
        a = b 
        b = c 
  
# Code to initiate the Fibonacci Sequence  
fibonacciTable(7)

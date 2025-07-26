for i in range(5):
    print(i)  

for i in range(2, 7):
    print(i)  

for i in range(1, 10, 2):
    print(i)  
for i in range(5, -1, -1):
    print(i) 
    
try:
    for i in range(0.5, 5.5):
        print(i)
except TypeError as e:
    print(f"Error: {e}") 

# Program that Constructs a Star Pyramid
    
def triangle(n): 
      
    # Number of Spaces Before and After Stars in the Triangle  
    k = 2*n - 2
  
    # Outer Loop to Handle the Number of Rows in the Pyramid   
    for i in range(0, n): 
      
        # This loop handles the number of spaces on each row  
        # Values that change according to each requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # Decrementing after each loop that builds each row of stars.   
        k = k - 1
      
        # Inner loop to handle the amount of columns in the pyramid 
        # The values change according to the outer loop
        for j in range(0, i+1): 
          
            # Printing stars
            print("* ", end="") 
      
        # Ending a line after each row
        print("\r") 
  
# Code that prompts the building of the pyramid  
n = 10
triangle(n) 
# Calculation of PI using Leibniz formula

# Function to calcultae PI using Leibniz
def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i /(2*i+1)
        t_sum = t_sum + term
    
    return t_sum * 4

# Reading number of terms to be considered in Leibniz formula
terms = int(input("Enter number of terms: "))

# Function call
pi = leibniz(terms)

# Displaying result
print("Pi = ", pi)

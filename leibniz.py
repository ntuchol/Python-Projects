def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = (-1) ** i /(2*i+1)
        t_sum = t_sum + term
    
    return t_sum * 4

terms = int(input("Enter number of terms: "))
pi = leibniz(terms)
print("Pi = ", pi)

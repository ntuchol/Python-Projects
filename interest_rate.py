def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

principal = 1000  
rate = 5          
time = 2         

si = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: ${si:.2f}")

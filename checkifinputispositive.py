def is_positive(num):
  
  return num > 0

user_input = input("Enter a number: ")
try:
  number = float(user_input)
  if is_positive(number):
    print(f"{number} is a positive number.")
  else:
    print(f"{number} is not a positive number.")
except ValueError:
  print("Invalid input. Please enter a valid number.")

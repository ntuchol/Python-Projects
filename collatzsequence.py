def collatz(number):
while number != 1:
if number % 2 == 0:
number = number // 2
else:
number = 3 * number + 1
print(number)

number = int(input("Enter a number: "))
collatz(number)
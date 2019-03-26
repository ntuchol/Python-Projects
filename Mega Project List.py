#https://github.com/rlingineni/PythonPractice/blob/master/piCalc/pi.py
#coding:utf-8

#Numbers- Finding PI to the Nth Digit 
"""
Pi = SUM k=0 to infinity 16^-k [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ]
"""
from __future__ import division
import math
from decimal import Decimal as D
from decimal import getcontext

getcontext().prec = 400
MAX = 10000
pi = D(0)

for k in range(MAX):
    pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))

print('PI >>>>>>>>>>' , pi)

#Finding e to the Nth Digit
from math import e

def e_with_precision(n):
    """Return euler's number to the n-th decimal place
    :param n: number of decimal places to return
    :type n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return '%.*f' % (n, e)

if __name__ == '__main__':
    # there is no do while loop in python, so we need to improvise
    correct_input = False
    while not correct_input:
        # ask until you get correct input
        print('Precision must be between 1 and 51')
        precision = int(input('Number of decimal places: '))
        if 51 >= precision > 0:
            correct_input = True
    print(e_with_precision(precision))
    
#Next Prime Number
choice = raw_input("Continue finding prime numbers (y/n)? ")
current = 1

def is_prime(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False

	return True

while choice.lower().startswith('y'):
	current += 1

	while is_prime(current) == False:
		current += 1

	print "Next prime is " + str(current)
	choice = raw_input("Continue finding prime numbers (y/n)? ")
    
#Find Cost of Tile to Cover WxH 
width = float(raw_input("Width of floor: "))
length = float(raw_input("Length of floor: "))
cost = float(raw_input("Cost of Tile: "))

print("Cost to tile a %.2f x %.2f floor is: $%.2f" % (width, length, width * length * cost));

#The Luhn Algorithm
def validate(n):
	
	intArray = intToArray(n)

	if len(intArray) % 2 == 0:
		oddEven(0, intArray)
	else:
		oddEven(1, intArray)

	if sum(intArray) % 10 == 0:
		return True
	else:
		return False

def intToArray(n):
	myArray = str(n)

	intArray = []
	for x in myArray:
		intArray.append(int(x))

	return intArray
    
#Doubles and sums array values
#Odd numbers have startIndex 1
def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 10:
            intArray[i] = newDigit
        else:
            intArray[i] = sumOfDigits(newDigit)
            
def sumOfDigits(n):
    return (n / 10) + (n % 10)

print validate(input("Enter CC number to validate\r\n>"))


        

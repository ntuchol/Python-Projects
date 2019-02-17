#Project Euler 

#Problem 1 
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.
def compute():
	answer = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(answer)


if __name__ == "__main__":
	print(compute())

#Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib = 1
fib2 = 2
temp = 0
total = 0

while temp <=4000000:
    temp = fib2
    if temp % 2 == 0:
        total += temp
    temp = fib + fib2
    fib = fib2
    fib2 = temp

print(total)

#Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.  What is the largest prime factor of the number 600851475143?
num = 600851475143
i = 2
while i * i < num:
     while num % i == 0:
         num = num / i
     i = i + 1
print(num)

#Problem 4 
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)

#Problem 5 
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def prob5():
  i = 20
  while 1:
    i+=20
    if i%11 == 0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19 == 0:
        print(i)
        break

#Problem 6 
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0
for i in range(101):
    sum = sum + i**2
print(sum)

squaresum = 0
for i in range(101):
    squaresum += i
print(squaresum ** 2)

answer = squaresum ** 2 - sum
print(answer)

#Problem 7 
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  What is the 10 001st prime number?
def eratosthenes():
    D = {}  
    q = 2   
    while 1:
        if q not in D:
            yield q        
            D[q*q] = [q]   
        else:
            for p in D[q]: 
                D.setdefault(p+q,[]).append(p)
            del D[q]       
        q += 1

def nth_prime(n):
    for i, prime in enumerate(eratosthenes()):
        if i == n - 1:
            return prime

print(nth_prime(10001))

#Problem 8 
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
import time
start = time.time()

num = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

biggest = 0
i = 0
while i < len(num) - 4:
    one = int(num[i]) 
    two = int(num[i+1])  
    thr = int(num[i+2]) 
    fou = int(num[i+3])
    fiv = int(num[i+4])
    product = one*two*thr*fou*fiv
    if product > biggest:
        biggest = product
    i = i + 1 
print(biggest)

#Problem 9 
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
for a in range(3, 1000):
    for b in range (a + 1, 999):
        cSquared = a**2 + b**2
        c = cSquared**0.5

        if a + b + c == 1000:
            product = a * b * c
            print(product)
            break

#Problem 10 
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.
def isPrime(n):
    if n < 2: 
      return("Neither prime, nor composite")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        sum += i

print (sum)
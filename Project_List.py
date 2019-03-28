#Prime_Factors
n = 600851475143
i = 2
while(i * i < n):
     while(n % i == 0):
         n = n / i
     i = i + 1
print (n)

#Cost of Tile Calculator 
costToCover = lambda w,h,ppm: w*h*ppm
print(costToCover(50,100,0.5))

def find_max_comb(seq):
    temp = 0
    for i,n in enumerate(seq):
        for v in seq[i+1:]:
            temp = max(temp,n+v)
    return temp

print(find_max_comb([1,7,3,1,3,5,4]))

#Caesar cipher
#Implement a Caesar cipher, both encoding and decoding. The key is an integer
#from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
#encoding replaces each letter with the 1st to 25th next letter in the alphabet
#(wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
#"BC". This simple "monoalphabetic substitution cipher" provides almost no
#security, because an attacker who has the encoded message can either use
#frequency analysis to guess the key, or just try all 25 keys.
#"""


class Caesar():

    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                self.translated = self.translated + self.LETTERS[num]
            else:
                self.translated = self.translated + symbol

        return self.translated

    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')

if __name__ == '__main__':
    cipher = Caesar()
    print cipher.encrypt(message='Secret message.', key=13)
    print cipher.decrypt(message='FRPERG ZRFFNTR.', key=13)


#Mortgage Calculator
loanAmount = input("How much do you want to borrow? \n")
interestRate = input("What is the interest rate on your loan? \n")
repaymentLength = input("How many years to repay your loan? \n")

#converting the string input variables to float
loanAmount = float(loanAmount)
interestRate = float(interestRate)
repaymentLength = float(repaymentLength)

#working out the interest rate to a decimal number
interestCalculation = interestRate / 100

print(interestRate)
print(interestCalculation)

#working out the number of payments over the course of the loan period.
numberOfPayments = repaymentLength*12

#Change Calculator
print("Change Calculator")

quarter = .25
dime = .10
nickel = .5
penny = .1

moneygiven = raw_input("Enter how much money given: ")
citem = raw_input("How much did the item cost?: ")
moneygiven = float(moneygiven)
citem = float(citem)
moneyback = moneygiven - citem

qmb = moneyback % quarter
partialtotal = moneyback - qmb * quarter 
dmb = partialtotal / dime
dpartialtotal = partialtotal - dmb * dime
nmb = dpartialtotal / nickel
npartialtotal = dpartialtotal - nmb * nickel
pmb = npartialtotal / penny
ppartialtotal = npartialtotal - pmb * penny

print("You need %s quarters, %s dimes, %s nickels, %s pennies." % (qmb, dmb, nmb, pmb))



# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            print p

from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:  
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else f"{self.numerator}"

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)

print("Addition:", fraction1 + fraction2)
print("Subtraction:", fraction1 - fraction2)
print("Multiplication:", fraction1 * fraction2)
print("Division:", fraction1 / fraction2)

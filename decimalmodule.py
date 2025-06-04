import decimal
from decimal import Decimal

# Setting precision
decimal.getcontext().prec = 6

# Creating Decimal instances
a = Decimal('1.1')
b = Decimal('2.2')

# Performing arithmetic operations
result = a + b
print(result) # Output: 3.3
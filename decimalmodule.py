import decimal
from decimal import Decimal

decimal.getcontext().prec = 6

a = Decimal('1.1')
b = Decimal('2.2')

result = a + b
print(result) # Output: 3.3

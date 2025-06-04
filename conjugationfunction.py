def conjugate_complex_number(z):
    return z.conjugate()
    
z1 = 2 + 3j
z1_conjugate = conjugate_complex_number(z1)
print(z1_conjugate)
# Expected output: (2-3j)

z2 = 1 - 1j
z2_conjugate = conjugate_complex_number(z2)
print(z2_conjugate)
# Expected output: (1+1j)

import numpy as np
z3 = np.array([4 + 5j, 6 - 7j])
z3_conjugate = np.conjugate(z3)
print(z3_conjugate)
# Expected output: [4.-5.j 6.+7.j]
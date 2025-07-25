def conjugate_complex_number(z):
    return z.conjugate()
    
z1 = 2 + 3j
z1_conjugate = conjugate_complex_number(z1)
print(z1_conjugate)

z2 = 1 - 1j
z2_conjugate = conjugate_complex_number(z2)
print(z2_conjugate)

import numpy as np
z3 = np.array([4 + 5j, 6 - 7j])
z3_conjugate = np.conjugate(z3)
print(z3_conjugate)

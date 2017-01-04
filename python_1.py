# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:37:57 2017

@author: Natalia Tucholska
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,10,25)
b = np.sin(a)

plt.plot(a,b, 'b^')
plt.grid(True)


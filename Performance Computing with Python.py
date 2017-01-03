# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 00:24:29 2017

@author: Natalia Tucholska
"""

loops = 25000000
from math import *
import numpy as np
import numexpr as ne

a = range(1, loops)
def f(x):
    return 3 * log(x) + cos(x) ** 2
%timeit r = [f(x) for x in a]

a = np.arange(1, loops)
%timeit r = 3 * np.log(a) + np.cos(a) ** 2

ne.set_num_threads(1)
f = ‘3 * log(a) + cos(a) ** 2'
%timeit r = ne.evaluate(f)

ne.set_num_threads(4)
%timeit r = ne.evaluate(f)


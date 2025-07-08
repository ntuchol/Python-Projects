import pandas as pd
import numpy as np

car_loan = 10000
interest = 0.07
years = 5
car_payments = np.pmt(rate = interest, nper = years, pv = -car_loan)
print(car_payments)
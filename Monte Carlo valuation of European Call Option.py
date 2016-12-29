#Monte Carlo valuation of European call option
# in Black-Scholes-Merton model

import numpy as np
# Parameter Values
S0 = 100 # initial index level
K = 105 # strike price
T = 1.0 # time-to-maturity
r = 0.05 # riskless short rate
sigma = 0.2 # volatility
I = 100000 # number of simulations
# Valuation Algorithm
z = np.random.standard_normal(I) # 1.drawing pseudorandom numbers from a standard normal distribution 
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)#2. Calculating stock index level at time T- or Black Scholes- Merton index level at maturity
# index values at maturity
hT = np.maximum(ST - K, 0) #5.Calculates all inner values of option at maturity
C0 = np.exp(-r * T) * np.sum(hT) / I #6. Calculates Monte Carlo estimator
# 7. Result Output
print("Value of the European Call Option %5.3f" % C0)
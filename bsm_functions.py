# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:16:08 2017

@author: Natalia Tucholska
"""
#
#Valution of European call options in Black-Scholes-Merton model
#incl. Vega function and implied volatility estimation 
#bsm_functions.py
#

#Analytical Black-Scholes-Merton (BSM) Formula 

def bsm_call_value(S0, K, T, r, sigma):
    from math import log, sqrt, exp
    from scipy import stats
    s0 = float(s0)
    d1 = (log(S0/K) + (r + 0.5*sigma**2) * T) / (sigma*sqrt(T))
    d2 = (log(S0/ K) + (r - 0.5*sigma**2) * T) / (sigma *sqrt(T))
    
    value = (S0*stats.norm.cdf(d1, 0.0, 1.0)) - K * exp(-r*T)* stats.norm.cdf(d2,0.0,1.0))
    #stats.norm.cdf--> cumulative distribution function for normal distribution
    return value 
  
    
#Vega function 
def bsm_vega(S0, K, T, r, sigma):
    from math import log, sqrt
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0/K) + (r+0.5*sigma**2) * T / (sigma*sqrt(T)))
    vega = s0 *stats.norm.cdf(d1,0.0, 1.0) *sqrt(T)
    return vega
    
#Implied volatility function
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it = 100):
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0))/ bsm_vega(S0, K, T, r, sigma_est)
    return sigma_est
    
    
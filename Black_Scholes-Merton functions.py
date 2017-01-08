options_data['IMP_VOL'] = 0.0 
from bsm_functions import *
tol = 0.5  
for option in options_data.index:
    forward = futures_data[futures_data]['Maturity'] == \ 
        options_data.loc[option][['Maturity']]['Price'].values[0]
        if(forward*(1-tol) < options_data.loc[option]['STRIKE']) < forward*(1+tol)):
    imp_vol = bsm_call_imp_vol(
                               V0,
                               options_data.loc[option]['STRIKE'],
                               options_data.loc[option]['TIM'],
                               r,
                               options_data.loc[option]['PRICE'],
                               sigma_est = 2., # estimate for implied volatility
                               it = 100)
    options_data['IMP_VOL'].loc[option] = imp_vol
    futures_data['MATURITY']
    options_data.loc[46170]
    options_data.loc[46170]['STRIKE']
    plot_data = options_data[options_data['IMP_VOL'] > 0]
    maturities = sorted(set(options_data['Maturity']))
    maturities 
    
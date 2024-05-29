import numpy as np
from scipy.stats import norm

def black_scholes_calc(S0, K, r, T, sigma, option_type='call'):
    '''This function calculates the value of the European option based on the Black-Scholes formula.
    - S0 = underlying asset price
    - K = strike price
    - r = risk-free rate
    - T = time to mature
    - sigma = implied volatility of the underlying asset
    - option_type = type of option to be calculated (ex: call or put) '''

    #1) Determine N(d1) and N(d2)
    d1 = 1/(sigma*np.sqrt(T)) * (np.log(S0/K) + (r+sigma**2/2)*T)
    d2 = d1 - sigma*np.sqrt(T)

    nd1 = norm.cdf(d1)
    nd2 = norm.cdf(d2)

    n_d1 = norm.cdf(-d1)
    n_d2 = norm.cdf(-d2)

    #2) Determine call value
    c = nd1*S0 - nd2*K*np.exp(-r*T)

    #3) Determine put value
    p = K*np.exp(-r*T)*n_d2 - S0*nd1

    #4) Define which value to return based on the option_type parameter
    if option_type=='call':
        return c
    elif option_type=='put':
        return p
    else:
        print('Wrong option type specified')

# Example usage
S0 = 100  # underlying asset price
K = 100   # strike price
r = 0.05  # risk-free rate
T = 1     # time to maturity
sigma = 0.2  # implied volatility

# Calculate call option value
call_value = black_scholes_calc(S0, K, r, T, sigma, option_type='call')
print("Call option value:", call_value)

# Calculate put option value
put_value = black_scholes_calc(S0, K, r, T, sigma, option_type='put')
print("Put option value:", put_value)

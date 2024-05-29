# Black-Scholes-Model-Calculator
This repository contains a Python script implementing the Black-Scholes formula for calculating the value of European options. The Black-Scholes formula is widely used in financial markets for pricing options contracts. 

# Black-Scholes Option Pricing

This Python script implements the Black-Scholes formula for calculating the value of European options. The Black-Scholes formula is a mathematical model used in finance for pricing options contracts.

## Overview

The Black-Scholes formula calculates the theoretical price of a European call or put option. It takes into account parameters such as the current price of the underlying asset, the strike price, the risk-free interest rate, the time to maturity, and the volatility of the underlying asset.

This script provides a simple interface to calculate the value of both call and put options using the Black-Scholes formula.

## Usage

To use this script, simply call the `black_scholes_calc` function with the required parameters:
- `S0`: Current price of the underlying asset
- `K`: Strike price of the option
- `r`: Risk-free interest rate
- `T`: Time to maturity (in years)
- `sigma`: Volatility of the underlying asset
- `option_type`: Type of option to be calculated ('call' or 'put')

Example usage:
```python
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

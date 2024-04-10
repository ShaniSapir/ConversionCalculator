# convert_dollar_to_shekel.py

import conversionRates

def convert_dollar_to_shekel(amount):
    # Retrieve conversion rate from conversionRates module
    conversion_rate = conversionRates['USD']
    # Perform conversion
    return amount * conversion_rate

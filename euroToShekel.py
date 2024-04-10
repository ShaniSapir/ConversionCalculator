# convert_euro_to_shekel.py

import conversionRates

def convert_euro_to_shekel(amount):
    # Retrieve conversion rate from conversionRates module
    conversion_rate = conversionRates['EUR']
    # Perform conversion
    return amount * conversion_rate

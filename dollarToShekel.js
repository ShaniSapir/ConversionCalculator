// dollarToShekel.js

const conversionRates = require('./conversionRates');

function convertDollarToShekel(amount) {
    // Check if 'USD' property exists in conversionRates
    if ('USD' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['USD'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for USD is not defined');
    }
}

module.exports = convertDollarToShekel; // Export the function

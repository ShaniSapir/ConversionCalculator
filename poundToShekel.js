// poundToShekel.js

const conversionRates = require('./conversionRates');

function convertPoundToShekel(amount) {
    // Check if 'GBP' property exists in conversionRates
    if ('GBP' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['GBP'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for GBP is not defined');
    }
    // Retrieve conversion rate from conversionRates module
}

module.exports = convertPoundToShekel; // Export the function
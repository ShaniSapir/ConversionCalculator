// euroToShekel.js

const conversionRates = require('./conversionRates');

function convertEuroToShekel(amount) {
    // Check if 'EUR' property exists in conversionRates
    if ('EUR' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['EUR'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for EUR is not defined');
    }
}

module.exports = convertEuroToShekel; // Export the function
// euroToShekel.js

const conversionRates = require('./conversionRates');

function convertWonToShekel(amount) {
    // Check if 'KRW' property exists in conversionRates
    if ('KRW' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['KRW'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for KRW is not defined');
    }
}

module.exports = convertWonToShekel; // Export the function
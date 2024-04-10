// dollarToShekel.js

const conversionRates = require('./conversionRates');

function convertWineToShekel(amount) {
    // Check if 'WINE' property exists in conversionRates
    if ('WINE' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['WINE'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for WINE is not defined');
    }
}

module.exports = convertWineToShekel; // Export the function
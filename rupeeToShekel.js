// dollarToShekel.js

const conversionRates = require('./conversionRates');

function convertRupeeToShekel(amount) {
     // Check if 'INR' property exists in conversionRates
     if ('INR' in conversionRates) {
        // Retrieve conversion rate from conversionRates module
        const conversionRate = conversionRates['INR'];
        // Perform conversion
        return amount * conversionRate;
    } else {
        throw new Error('Conversion rate for INR is not defined');
    }
}

module.exports = convertRupeeToShekel; // Export the function
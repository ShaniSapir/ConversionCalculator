// displayRates.js

// Import the conversion rates from conversionRates.js
const conversionRates = require('./conversionRates');

function displayRates() {
    let tableHTML = "<table>";
    tableHTML += "<tr><th>Currency</th><th>Rate</th></tr>";
    for (const currency in conversionRates) {
        tableHTML += `<tr><td>${currency}</td><td>${conversionRates[currency]}</td></tr>`;
    }
    tableHTML += "</table>";
    return tableHTML;
}

module.exports = displayRates; // Export the function


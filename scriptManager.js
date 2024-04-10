const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Include your conversion functions and rates here
const displayRates = require('./displayRates');
const convertDollarToShekel = require('./dollarToShekel');
const convertEuroToShekel = require('./euroToShekel');
const convertPoundToShekel = require('./poundToShekel');
const convertRupeeToShekel = require('./rupeeToShekel');
const convertWineToShekel = require('./wineToShekel');
const convertWonToShekel = require('./wonToShekel');


// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));

// Serve HTML file with conversion form
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Handle conversion request
app.get('/convert/:conversionType/:amount', (req, res) => {
  try {
    const { conversionType, amount } = req.params;
    const convertedAmount = convertAmount(conversionType, parseFloat(amount));
    res.send(convertedAmount.toString()); // Send the converted amount back to the client
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});
// Function to convert the amount based on the conversion type
function convertAmount(conversionType, amount) {
  switch (conversionType) {
    case 'dollarToShekel':
      return convertDollarToShekel(amount);
    case 'euroToShekel':
      return convertEuroToShekel(amount);
    case 'poundToShekel':
      return convertPoundToShekel(amount);
    case 'rupeeToShekel':
      return convertRupeeToShekel(amount);
    case 'wineToShekel':
      return convertWineToShekel(amount);
    case 'wonToShekel':
        return convertWonToShekel(amount);
    default:
      throw new Error('Invalid conversion type');
  }
}

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

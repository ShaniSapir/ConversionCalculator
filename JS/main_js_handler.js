// Import dotenv and call config to load the .env file
require('dotenv').config();

// Import express
const express = require('express');
const configs_path = 'configs.json'
const fs = require('fs');
const conversions = JSON.parse(fs.readFileSync(configs_path, 'utf8')).conversions;

// Create an instance of express
const app = express();
// Middleware to parse JSON bodies
app.use(express.json());
// Get the port from the environment variables or use 3002 as a default
const port = process.env.JS_HANDLER_PORT || 3002;

function is_float(val){
  return !isNaN(parseFloat(val))
}
function convert(val, mult){
  return parseFloat((parseFloat(val) * mult).toFixed(2))
}
function handle_conversion(req, res, mult){
  const val  = req.body.value;
  if(val === "" || val === undefined || val === null){
    res.status(400).json({results : 0, error:"Missing value"})
    return
  }
  if(!is_float(val)){
    res.status(400).json({results : 0, error:"Value not numeric"})
    return
  }
  res.status(200).json({results : convert(val,mult)});
}

app.post('/dollar_shekel', (req, res) => {
  handle_conversion(req,res, conversions.dollar_shekel)
});
app.post('/euro_shekel', (req, res) => {
  handle_conversion(req,res, conversions.euro_shekel)
});
app.post('/pound_shekel', (req, res) => {
  handle_conversion(req,res, conversions.pound_shekel)
});
app.post('/yen_shekel', (req, res) => {
  handle_conversion(req,res, conversions.yen_shekel)
});
app.post('/rupee_shekel', (req, res) => {
  handle_conversion(req, res, conversions.rupee_shekel)
});
app.post('/wan_shekel', (req, res) => {
  handle_conversion(req, res, conversions.wan_shekel)
});

// Start the server
app.listen(port, "0.0.0.0", () => {
  console.log(`listening at http://localhost:${port}`);
});

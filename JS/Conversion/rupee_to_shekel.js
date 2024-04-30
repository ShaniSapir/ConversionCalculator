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
const port = process.env.JS_RUPPE_TO_SHEKEL_PORT || 3006;

function is_float(val){
  return !isNaN(val)
}
function convert(val, mult){
  return parseFloat((parseFloat(val) * mult).toFixed(2))
}
function handle_conversion(req, res, mult){
  const val  = req.body.value;
  if(val === '' || val === "" || val === undefined || val === null){
    res.status(400).json({results : 0, error:"Missing value"})
    return
  }
  if(!is_float(val)){
    res.status(400).json({results : 0, error:"Value not numeric"})
    return
  }
  res.status(200).json({results : convert(val,mult)});
}
app.post('/', (req, res) => {
  handle_conversion(req,res, conversions.rupee_shekel)
});


// Start the server
app.listen(port, "0.0.0.0", () => {
  console.log(`listening at http://localhost:${port}`);
});

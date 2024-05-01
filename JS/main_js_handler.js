require('dotenv').config();
const express = require('express');
const fetch = require("node-fetch");

const localhost = "http://dockernet:"

// Create an instance of express
const app = express();
// Middleware to parse JSON bodies
app.use(express.json());
// Get the port from the environment variables or use 3002 as a default
const port = process.env.JS_HANDLER_PORT || 3002;

function is_float(val){
  return !isNaN(val)
}
function convert(val, mult){
  return parseFloat((parseFloat(val) * mult).toFixed(2))
}
function handle_conversion(req, res, url){
const body = req.body
console.log(body)
fetch(url, {
  method: 'POST',  
  headers: {
      'Content-Type': 'application/json' 
  },
  body: JSON.stringify(body)
})
.then(response => {res.status(response.status);
   return response.json();})
.then(js => {console.log(js); res.json(js);}) 
.catch(error => {
  console.log(error)
  res.status(400).json({results : 0, error:"Server not found"});
});  // Log any errors
}

app.post('/dollar_shekel', (req, res) => {
  handle_conversion(req, res, "http://js-dollar-shekel:"+process.env.JS_DOLLAR_TO_SHEKEL_PORT)
});
app.post('/euro_shekel', (req, res) => {
  handle_conversion(req, res,"http://js-euro-shekel:"+ process.env.JS_EURO_TO_SHEKEL_PORT)
});
app.post('/pound_shekel', (req, res) => {
  handle_conversion(req, res,"http://js-pound-shekel:"+ process.env.JS_POUND_TO_SHEKEL_PORT)
});
app.post('/yen_shekel', (req, res) => {
  handle_conversion(req, res, "http://js-yen-shekel:"+process.env.JS_YEN_TO_SHEKEL_PORT)
});
app.post('/rupee_shekel', (req, res) => {
  handle_conversion(req,res, "http://js-rupee-shekel:"+process.env.JS_RUPEE_TO_SHEKEL_PORT)
});
app.post('/wan_shekel', (req, res) => {
  handle_conversion(req,res, "http://js-wan-shekel:"+process.env.JS_WAN_TO_SHEKEL_PORT)
});

// Start the server
app.listen(port, "0.0.0.0", () => {
  console.log(`listening at http://localhost:${port}`);
});

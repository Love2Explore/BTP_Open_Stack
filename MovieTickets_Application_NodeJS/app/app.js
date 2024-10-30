const express = require("express");
const mongoose = require("mongoose");
const router = express.Router();
const movie_route = require("./routes/movietickets");
const path = require("path");
const bodyparser = require("body-parser");

const app = express();

app.use(express.json())
app.use(express.urlencoded({extended:true}))

//Routes should be added after middleware like express.json() 
app.use(movie_route);



mongoose.connect("mongodb+srv://workportal1992:gFYgIJRE5WZHc5yf@cluster0.a7j0f.mongodb.net/myDB?retryWrites=true&w=majority")

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log("Express App running at http://127.0.0.1:3000/");
})

  
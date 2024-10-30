const { getDatabase } = require('../util/database');
const ObjectId = require('mongodb').ObjectId;
const Ticket = require("../model/ticket");

exports.getTicket =  function(req,res) {
    try {
        //var query = { "_id": new  ObjectId(req.query.ticket)};
         Ticket.findById(req.query.ticket)
         .then(result=>{
            res.send(result);
         });
        
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

exports.getAllTicket =  function(req,res) {
    try {
         Ticket.find()
         .then(result=>{
            res.send(result);
         });
        
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

exports.postTicket =  function(req,res,next) {
    try {
        var ticket = new Ticket({ title: req.body.title, price: req.body.price , description:req.body.description , movie:req.body.movie });
        ticket.save()
         .then(result=>{
            res.send(result);
         });
        
    } catch (error) {
        console.error('Error saving data:', error);
        res.status(400).send("Error");
    }
}


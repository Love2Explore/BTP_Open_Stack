const mongoose = require('mongoose');
const { getDatabase } = require('../util/database');

mongoose.connection.useDb(getDatabase)

const Schema = mongoose.Schema;
const ticketSchema = new Schema({
  title: { 
    type:String ,
    required: true
  },
  price:{
    type:String ,
    required: true
  },
  description:{
    type:String ,
    required:true
  },
  movie:{
    type:String,
    reuired:true
  }
});

module.exports = mongoose.model('movietickets', ticketSchema);
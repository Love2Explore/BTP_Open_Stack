const express = require('express')
const router = express.Router();
const ticketController  = require('../controllers/movietickets')


router.get('/asmbtp/get-ticket',ticketController.getTicket)
router.get('/asmbtp/get-all-ticket',ticketController.getAllTicket)
router.post('/asmbtp/post-ticket',ticketController.postTicket) 

router.get('/', function (req, res) {
    res.send('Hello World');
 })


module.exports = router
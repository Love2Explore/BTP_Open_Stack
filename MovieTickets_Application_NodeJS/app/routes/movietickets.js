const express = require('express')
const router = express.Router();
const ticketController  = require('../controllers/movietickets')


router.get('/ticket/get-ticket',ticketController.getTicket)
router.get('/ticket/get-all-ticket',ticketController.getAllTicket)
router.post('/ticket/post-ticket',ticketController.postTicket) 

router.get('/', function (req, res) {
    res.send('Hello World');
 })


module.exports = router
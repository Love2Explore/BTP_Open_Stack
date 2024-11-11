### PYTHON API Documentation
* User API
    * Create USER <br />
    ###
	    --POST https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user 
		   BODY 
		                { 
		                    "username":"user", 
		                    "password":"password" 
		                } 
      
    * Read User <br />
    ###
  		--GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user?username=name 
		--GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user?id=6708bf500b25473e41e909f0 
* Booking API
    * Booking Tickets
    ###
        --POST https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/booking 
		   BODY
		                {
                            "username":"user",
                            "movie_id":"6708bf500b25473e41e909f0"
                        }
    * Read Bookings
    ###
        --GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/booking?id=6708bf500b25473e41e909f0
    
### NODEJS API Documentation
* Tickets API
    * Create Movie Tickets
    ###
        --POST https://ticketbooking-wise-lemur-dk.cfapps.us10-001.hana.ondemand.com/asmbtp/post-ticket
            BODY
                    {
                        "title": "Bat Man Ticket", 
                        "price": "20$" , 
                        "description":"Ticket for One Movie" , 
                        "movie":"Bat Man"
                    }
    * Get One Movie Tickets
    ###
        --GET https://movietickets-reflective-bushbuck-yu.cfapps.us10-001.hana.ondemand.com/asmbtp/get-ticket?ticket=6708bf500b25473e41e909f0
    * Get ALL Movie Tickets
    ###
        --GET https://movietickets-reflective-bushbuck-yu.cfapps.us10-001.hana.ondemand.com/asmbtp/get-all-ticket
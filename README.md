### PYTHON API Documentation
* User API
    * Create USER <br />
    ###
	    --POST https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user <br />
		   BODY <br />
		                { <br />
		                    "username":"user", <br />
		                    "password":"password" <br />
		                } <br />
      
    * Read User <br />
    ###
  		--GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user?username=name <br />
		--GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/user?id=6708bf500b25473e41e909f0 <br />
* Booking API
    * Booking Tickets
    ###
        --POST https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/booking <br />
		   BODY <br />
		                {
                            "username":"rahul",
                            "movie_id":"6708bf500b25473e41e909f0"
                        }
    * Read Bookings
    ###
        --GET https://ticketbooking-cheerful-jackal-xl.cfapps.us10-001.hana.ondemand.com/asmbtp/booking?id=6708bf500b25473e41e909f0 <br />
    
### NODEJS API Documentation
* Tickets API
    * Create Movie Tickets
    ###

    * Get Movie Tickets
    ###

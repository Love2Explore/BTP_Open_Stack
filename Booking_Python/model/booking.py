
class BookingModel: 
    def __init__(self,username,movie_id):
        self.username = username
        self.movie_id = movie_id

    def to_dict(self):
        return {"username":self.username , "movie_id":self.movie_id}   



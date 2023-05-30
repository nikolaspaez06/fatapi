from models.rating import Rating as RatingModel

class RatingService():
    def __init__(self, db):
        self.db = db
        
    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result
    
    def  create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            mov_id = rating.gen_id,
            rev_id = rating.gen_id,
            rev_star = rating.gen_star,
            num_o_ratings = rating.gen_num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(RatingModel).filter(RatingModel.id == id). first()
        return result
    
    def update_rating(self,data):
        rating = self.db.query(RatingModel).filter(RatingModel.id == data.id). first()
        rating.mov_id = data.mov_id
        rating.rev_id= data.rev_id
        rating.rev_star =data.rev_star
        rating.num_o_ratings = data.num_o_ratings   
        self.db.commit()
        return
    
    def delete_rating(self,id:int):
        self.db.query(RatingModel).filter(RatingModel.id == id).delete()
        self.db.commit()
        return
    
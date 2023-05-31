from models.Movie_Cast import Movie_Cast as Mov_CastModel


class Mov_Cast():
    def __init__(self,db):
        self.db = db

    def get_Mov_Cast(self):
        result = self.db.query(Mov_CastModel).all()
        return result

    def create_Movie_Cast(self,Mov_Cast: Mov_CastModel):
        new_Mov_Cast = Mov_CastModel(
            act_id = Mov_Cast.act_id,
            mov_id = Mov_Cast.mov_id,
            role = Mov_Cast.role.upper ()
        )
        self.db.add(new_Mov_Cast)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result= self.db.query(Mov_CastModel).filter(Mov_CastModel.id == id).first()
        return result
    
    def update_Movie_Cast(self,data:Mov_CastModel):
        Mov_Cast = self.db.query(Mov_CastModel).filter(Mov_CastModel.id == data.id).first()
        Mov_Cast.act_id = data.act_id
        Mov_Cast.mov_id = data.mov_id
        Mov_Cast.role= data.role
        self.db.commit()
        return
        
    
    def delete_Movie_Cast(self,id:int):
        self.db.query(Mov_CastModel).filter(Mov_CastModel.id == id).delete()
        self.db.commit()
        
    
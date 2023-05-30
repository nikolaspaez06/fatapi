from models.Mov_Cast import Mov_Cast as Mov_CastModel
from schemas.Movie_Cast import Mov_Cast

class Mov_Cast():
    def __init__(self,db):
        self.db = db

    def get_Mov_Cast(self):
        result = self.db.Query(Mov_CastModel).all()
        return result

    def create_Mov_Cast(self,Mov_Cast: Mov_CastModel):
        new_Mov_Cast = Mov_CastModel(
            act_id = Mov_Cast.dir_id,
            mov_id = Mov_Cast.mov_id,
            role = Mov_Cast.role.upper,
        )
        self.db.add(new_Mov_Cast)
        self.db.commit()
        return
    
    def get_for_id(self,data: Mov_CastModel):
        result= self.db.Query(Mov_CastModel).filter(Mov_CastModel.id == id).first()
        return result
    
    def update_Mov_Cast(self,data:Mov_CastModel):
        Mov_Cast = self .db.Query(Mov_CastModel).filter(Mov_CastModel == id).first()
        Mov_Cast.dir_id = data.act_id
        Mov_Cast.mov_id = data.mov_id
        Mov_Cast.role=data.Movie_Cast
        self.db.commit()
        return
    
    def delete_Mov_Cast(self,id:int):
        self.db.Query(Mov_Cast or Model).filter(Mov_CastModel.id == id).delete()
        self.db.commit()
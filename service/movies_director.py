from models.movie_director import Mov_Director as Mov_DirectorModel
from schemas.movie_director import Mov_Director

class Mov_Director():
    def __init__(self, db):
        self.db = db

    def get_mov_director(self):
        result = self.db.query(Mov_DirectorModel).all()
        return result

    def create_mov_director(self, mov_director: Mov_DirectorModel):
        new_mov_director = Mov_DirectorModel(
            dir_id=mov_director.dir_id,
            mov_id=mov_director.mov_id,
        )
        self.db.add(new_mov_director)
        self.db.commit()

    def get_for_id(self, id: int):
        result = self.db.query(Mov_DirectorModel).filter(Mov_DirectorModel.id == id).first()
        return result

    def update_mov_director(self, data: Mov_DirectorModel):
        mov_director = self.db.query(Mov_DirectorModel).filter(Mov_DirectorModel.id == data.id).first()
        mov_director.dir_id = data.dir_id
        mov_director.mov_id = data.mov_id
        self.db.commit()

    def delete_mov_director(self, did: int):
        mov_director = self.db.query(Mov_DirectorModel).filter(Mov_DirectorModel.id == did).first()
        if mov_director:
            self.db.delete(mov_director)
            self.db.commit()

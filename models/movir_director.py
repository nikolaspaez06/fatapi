from sqlalchemy import column, ForeignKey, Integer

from config import base 

class movieDirector(base):
    __tablename__ = "movie_director"

    id=column(interger,primary_key=True)
    dir_id = column(Integer,ForeignKey("dir_id"))
    movi_id = column(Integer,ForeignKey("mov.id"))
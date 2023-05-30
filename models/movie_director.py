from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base 

class Mov_Director(Base):
    __tablename__ = "mov_director"

    id=Column(Integer,primary_key=True)
    dir_id = Column(Integer,ForeignKey("director.id"))
    mov_id = Column(Integer,ForeignKey("movie.id"))


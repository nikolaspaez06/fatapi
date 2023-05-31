from sqlalchemy import Column, ForeignKey, Integer, String

from config.database import Base 

class Movie_Cast(Base):
    __tablename__ = "movie_cast"

    id=Column(Integer,primary_key=True)
    act_id = Column(Integer,ForeignKey("actor.id"))
    mov_id = Column(Integer,ForeignKey("movie.id"))
    role = Column(String(30))

    
from sqlalchemy import Column, ForeignKey, Integer, String

from config.database import Base 

class MovieCast(Base):
    __tablename__ = "movie_cast"

    id=Column(Integer,primary_key=True)
    act_id = Column(Integer,ForeignKey("actor_id"))
    mov_id = Column(Integer,ForeignKey("movies_id"))
    role = Column(String(30))
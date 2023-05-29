from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base 

class MovieDirector(Base):
    __tablename__ = "movie_director"

    id=Column(Integer,primary_key=True)
    dir_id = Column(Integer,ForeignKey("dir_id"))
    mov_id = Column(Integer,ForeignKey("mov.id"))


from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base 

class movieGenres(Base):
    __tablename__ = "movie_genres"

    id=Column(Integer,primary_key=True)
    gen_id = Column(Integer,ForeignKey("generes_id"))
    movie_id = Column(Integer,ForeignKey("movie.id"))
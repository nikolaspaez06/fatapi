from sqlalchemy import Column, ForeignKey, Integer

from config import base 

class movieGenres(base):
    __tablename__ = "movie_genres"

    id=Column(Integer,primary_key=True)
    gen_id = Column(Integer,ForeignKey("generes_id"))
    movie_id = Column(Integer,ForeignKey("movie.id"))





    
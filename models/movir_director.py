from sqlalchemy import column, ForeignKey, Integer

from config import base 

class MovieDirector(base):
    __tablename__ = "movie_director"

    id=column(interger,primary_key=True)
    dir_id = column(Integer,ForeignKey("dir_id"))
    movi_id = column(Integer,ForeignKey("mov.id"))


movie = relationship("movie", back_populates="movie_director")
director = relationship("director", back_populates="movie_director")
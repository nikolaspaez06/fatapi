from sqlalchemy import column, ForeignKey, Integer

from config import base 

class movieGenres(base):
    __tablename__ = "movie_genres"

    id=column(interger,primary_key=true)
    gen_id = column(Integer,ForeignKey("generes_id"))
    movie_id = column(Integer,ForeignKey("movie.id"))





    
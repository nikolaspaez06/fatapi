from sqlalchemy import column, ForeignKey,  Integer

from config import Base

class MovieGenres(Base):
    
    __tablename__ = "movie_genres"
    
    id = column(Integer, primary_key = True )
    gen_id = column(Integer, ForeignKey("genres.id"))
    movie_id = column(Integer, ForeignKey("movie.id"))
    
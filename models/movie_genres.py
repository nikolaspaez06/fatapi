from sqlalchemy import Column, ForeignKey,  Integer

from config import Base

class MovieGenres(Base):
    
    __tablename__ = "movie_genres"
    
    id = Column(Integer, primary_key = True )
    gen_id = Column(Integer, ForeignKey("genres.id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))
    
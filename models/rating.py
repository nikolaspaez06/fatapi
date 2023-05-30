from sqlalchemy import Column, ForeignKey,  Integer

from config.database import Base

class Rating(Base):
    
    __tablename__ = "Rating"
    
    id = Column(Integer, primary_key=True )
    mov_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.id"))
    rev_stars = Column(Integer)
    num_o_ratings = Column(Integer)
    
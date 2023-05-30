from sqlalchemy import Column, ForeignKey,  Integer

from config.database import Base

class Rating(Base):
    
    __tablename__ = "Rating"
    
    id = Column(Integer, primary_key=True )
    mov_id = Column(Integer, ForeignKey("mov.id"))
    rev_id = Column(Integer, ForeignKey("rev.id"))
    rev_stars = Column(Integer, ForeignKey("rev.stars"))
    num_o_ratings = Column(Integer, ForeignKey("num_o_ratings"))
    
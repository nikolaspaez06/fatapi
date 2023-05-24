from sqlalchemy import Column, ForeignKey,  Integer

from config.database import Base

class rating(Base):
    
    __tablename__ = "rating"
    
    id = Column(Integer, primary_key=True )
    mov_id = Column(Integer, ForeignKey("mov.id"))
    rev_id = Column(Integer, ForeignKey("rev.id"))
    rev_stars = Column(Integer, ForeignKey("rev.id"))
    num_o_ratings = Column(Integer, ForeignKey("num_o_ratings"))
    
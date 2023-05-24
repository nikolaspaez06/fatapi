from sqlalchemy import column, ForeignKey,  Integer

from config.database import Base

class rating(Base):
    
    __tablename__ = "rating"
    
    id = column(Integer, primary_key = True )
    mov_id = column(Integer, ForeignKey("mov.id"))
    rev_id = column(Integer, ForeignKey("rev.id"))
    rev_stars = column(Integer, ForeignKey("rev.id"))
    num_o_ratings = column(Integer, ForeignKey("num_o_ratings"))
    
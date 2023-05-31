from sqlalchemy import Column, Integer, String 
from config.database import Base
from sqlalchemy.orm import relationship

class Director(Base):
    
    __tablename__ = "director"
    
    id = Column(Integer, primary_key=True)
    dir_fname = Column(String(255))
    dir_iname = Column(String(255))
    
    movies_directors = relationship("Mov_Director", back_populates="director", foreign_keys='Mov_Director.dir_id')
    

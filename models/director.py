from sqlalchemy import Column, Integer, String 

from config.database import Base

class Director(Base):
    
    __tablename__ = "director"
    
    id = Column(Integer, primary_key=True)
    dir_fname = Column(String(255))
    dir_iname = Column(String(255))
    

from sqlalchemy import column, Integer, String 

from config.database import Base

class reviewer(Base):
    
    __tablename__ = "reviewer"
    
    id = column(Integer, primary_key = True)
    rev_name = column(String) 
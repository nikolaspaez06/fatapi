
from sqlalchemy import Column

from config.database import Base


class Genres(Base)
    
    _tablename_="genres"

    id= Column(Integer, primary_key=True)
    gen_tittle = Column(string)



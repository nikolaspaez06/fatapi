from sqlalchemy import Column, Integer, String

from config.database import Base


class Generes(Base):

    __tablename__ ="genere"
    id = Column(Integer,primary_key=True)

    gen_title = Column(String)

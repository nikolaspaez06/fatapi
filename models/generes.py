from sqlalchemy import column

from config.database import Base


class Generes(Base):

    __tablename__ ="genere"
    id = column(integer,primary_key=true)

    gen_title = column(string)

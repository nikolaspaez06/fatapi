from pydantic import BaseModel, Field

from typing import Optional

class MovieGenres(BaseModel):
   id : Optional[int] = None
   gen_id : int = Field(ge=1, description="id de genero")
   mov_id :int = Field(ge=1, description="llave foranea de peliculas")

   class Config:
        schemas_extra = {
            "example":{
                "gen_id":2,
                "movie_id":3
            }
        }
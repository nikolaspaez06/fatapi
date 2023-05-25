from pydantic import BaseModel, Field

from typing import Optional

class   Ratings(BaseModel):
   id : Optional[int] = None
   mov_id :int = Field(ge=1, description="llave foranea de peliculas")
   rev_id :int = Field(ge=1, description="Llave foranea de reviewer")
   rev_star :int = Field(ge=1, description="Star de reviewer")
   num_o_ratings :int = Field(ge=1, description="num_o_ratings")

   class Config:
        schemas_extra = {
            "example":{
                "movie_id":2,
                "rev_id":3,
                "rev_star":4,
                "num_o_ratings":5
                
            }
        }
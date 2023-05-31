from pydantic import BaseModel, Field

from typing import Optional

class   Movie_Cast(BaseModel):
   id : Optional[int] = None
   act_id :int = Field(ge=1, description="llave foranea de actores")
   mov_id :int = Field(ge=1, description="Llave foranea de pelicula")
   role : str = Field(max_length=30, min_length=1, description="papel que hace")
   

   class Config:
        schemas_extra = {
            "example":{
                "act_id":2,
                "mov_id":3,
                "role":"protagonista"
                
                
            }
        }
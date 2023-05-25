from pydantic import BaseModel, Field

from typing import Optional

class Mov_Director(BaseModel):
    id : Optional[int] = None
    dir_id:int = Field(ge=1, description="id del director")
    mov_id :int = Field(ge=1, description="llave foranea de la pelicula ")



    class Config:
        schemas_extra = {
            "example":{
                "dir_id":2,
                "mov_id":3

            }
        }
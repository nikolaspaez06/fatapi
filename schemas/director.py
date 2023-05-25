from pydantic import BaseModel, Field

from typing import Optional

class Director(BaseModel):
    id : Optional[int] = None
    dir_fname: str = Field(max_length=15,min_length=3,   description="nombre del director")
    dir_lname: str = Field(max_length=15,min_length=3,description="apellido del director")
    class Config:
        schemas_extra = {
            "example":{
                "id":1,
                "dir_fname":"tim",
                "dir_lname":"burthon"    
            }
        }
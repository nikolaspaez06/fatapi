from pydantic import BaseModel, Field
from typing import Optional

class Genres (BaseModel):
    id : Optional[int] = None
    gen_title : str  

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "gen_title":"Action"
            }
        }
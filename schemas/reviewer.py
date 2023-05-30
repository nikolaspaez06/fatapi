from pydantic import BaseModel, Field
from typing import Optional

class Reviewer (BaseModel):
    id : Optional[int] = None
    rev_name : str = Field(max_length=15, min_length=3, description="Nombre de crítico")

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "rev_name":"Cualquiera"
            }
        }
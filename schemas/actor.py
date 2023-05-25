from pydactic import BaseModel, Field

from typing import Optional

class actor(BaseModel):
    id: Optional[int] = None
    act_fname : str = Field(max_legth=20, min_length=3,description="actors name")
    act_lname : str = Field(max_legth=20, min_length=3,description="actors last name")
    act_gender : str = Field(max_legth=2, min_length=1,description="gender of the actors")
    

    class Config:
        schema_extra = {
            "example":{
                "id":1
                "act_fname":"leonardo"
                "act_lname":"dicaprio"
                "act_gender":"m"
            }
        }
        

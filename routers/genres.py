from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.genres import GenresService
from schemas.genres import Genres 
from config.database import Session

genres_router = APIRouter()

#@genres_router.get('/genres', tags=['genres'], status_code=200)
#def get_genres_hello():
    

@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_genres():
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code = 200)
    
    
@genres_router.get('/genres_id', tags=['genres'], status_code=200)
def get_genre_for_id(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
   

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres(genres:Genres):
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={"message":"genre created successfully", "status_code" : 201})


#para el genres delete debemos verificar que el id existe y depués ese genero lo eliminamos


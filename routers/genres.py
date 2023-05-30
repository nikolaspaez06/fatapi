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


@genres_router.put("/genres{id}",tags=["genres"])

@genres_router.put('/genres{id}', tags =['genres'])

def update_genre(id:int,genres:Genres):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:

        return JSONResponse(content={"message":"genre dont't found", "status_code":404})
    GenresService(db).update_genre(genres)
    return JSONResponse(content={"message":"genre update succeefully","status_code":202}, status_code=202)
    
    #todo editar
    
@genres_router.delete("/genres{id}",tags=["genres"])
def delete_genre(id:int,movie:Genres):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre dont't found", "status_code":404})
    GenresService(db).delete_genre(id)
    return JSONResponse(content={"message":"genre delete successfully", "status_code":200}, status_code=200)
    #todoeliminar
    

    return JSONResponse(content={"message":"genre don't gound", "status_code":404})
    GenresService(db).update_genre(genres)
    return JSONResponse(content={"message":"genre update successfully", "status_code": 202}, status_code=202)
    
@genres_router.delete('/genres{id}', tags =['genres'])
def delete_genre(id:int):
    db = Session()
    result = GenresService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't found", "status_code":404})
    GenresService(db).delete_genre(id)
    return JSONResponse(content={"message":"genre delete successfully", "status_code":200}, status_code=200)    
    
    



#para el genres delete debemos verificar que el id existe y depués ese genero lo eliminamos


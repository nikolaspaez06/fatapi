from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Movie_Cast import Movie_CastService
from schemas.Movie_Cast import Movie_Cast 
from config.database import Session

Movie_Cast_router = APIRouter()

    

@Movie_Cast_router.get('/Movie_Cast', tags=['Movie_Cast'], status_code=200)
def get_Movie_Cast():
    db = Session()
    result = Movie_CastService(db).get_Movie_Cast()
    return JSONResponse(content=jsonable_encoder(result), status_code = 200)
    
    
@Movie_Cast_router.get('/Movie_Cast_id', tags=['Movie_Cast'], status_code=200)
def get_Movie_Cast_for_id(id:int):
    db = Session()
    result = Movie_CastService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
   

@Movie_Cast_router.post('/Movie_Cast', tags=['Movie_Cast'], status_code=201)
def create_Movie_Cast(Movie_Cast:Movie_Cast):
    db = Session()
    Movie_CastService(db).create_Movie_Cast(Movie_Cast)
    return JSONResponse(content={"message":"Movie_Cast created successfully", "status_code" : 201})

@Movie_Cast_router.put('/Movie_Cast{id}', tags =['Movie_Cast'])
def update_Movie_Cast(id:int,Movie_Cast:Movie_Cast):
    db = Session()
    result = Movie_CastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"Movie_Cast don't gound", "status_code":404})
    Movie_CastService(db).update_Movie_Cast(Movie_Cast)
    return JSONResponse(content={"message":"Movie_Cast update successfully", "status_code": 202}, status_code=202)
    
@Movie_Cast_router.delete('/Movie_Cast{id}', tags =['Movie_Cast'])
def delete_Movie_Cast(id:int):
    db = Session()
    result = Movie_CastService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"Movie_Cast don't found", "status_code":404})
    Movie_CastService(db).delete_Movie_Cast(id)
    return JSONResponse(content={"message":"Movie_Cast delete successfully", "status_code":200}, status_code=200)
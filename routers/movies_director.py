from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from service.movies_director import Mov_Director as movi_directorService
from schemas.movie_director import Mov_Director as Mov_DirectorSchemas

mov_director_router = APIRouter()

@mov_director_router.get("/mov_director", tags=["mov_director"], status_code=200)
def get_mov_director():
    db = Session()
    result = movi_directorService(db).get_mov_director()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@mov_director_router.get("/mov_director_for_id", tags=["mov_director"], status_code=200)
def get_mov_director_for_id(id: int):
    db = Session()
    result = movi_directorService(db).get_for_id(id)
    return result

@mov_director_router.post("/mov_director", tags=["mov_director"], status_code=201)
def create_mov_director(movie_director: Mov_DirectorSchemas):
    db = Session()
    movi_directorService(db).create_mov_director(movie_director)
    return JSONResponse(content={"message": "mov_director created successfully", "status_code": 201}, status_code=201)

@mov_director_router.put('/mov_director/{id}', tags=['mov_director'])
def update_mov_director(id: int, data: Mov_DirectorSchemas):
    db = Session()
    result = movi_directorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "mov_director not found", "status_code": 404})
    movi_directorService(db).update_mov_director(data)
    return JSONResponse(content={"message": "mov_director updated successfully", "status_code": 200}, status_code=200)

@mov_director_router.delete("/mov_director/{id}", tags=["mov_director"])
def delete_mov_director(id: int):
    db = Session()
    result = movi_directorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "mov_director not found", "status_code": 404})
    movi_directorService(db).delete_mov_director(result)
    return JSONResponse(content={"message": "mov_director deleted successfully", "status_code": 200}, status_code=200)

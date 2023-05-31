from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.actor import ActorService
from schemas.actor import Actor
from config.database import Session

actor_router = APIRouter()

#@genres_router.get('/genres', tags=['genres'], status_code=200)
#def get_genres_hello():
    

@actor_router.get('/actor', tags=['actor'], status_code=200)
def get_actor():
    db = Session()
    result = ActorService(db).get_actor()
    return JSONResponse(content=jsonable_encoder(result), status_code = 200)
    
    
@actor_router.get('/actor_id', tags=['actor'], status_code=200)
def get_actor_for_id(id:int):
    db = Session()
    result = ActorService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@actor_router.post('/actor', tags=['actor'], status_code=201)
def create_actor(actor:Actor):
    db = Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={"message":" created successfully", "status_code" : 201})

@actor_router.put("/actor{id}",tags=["actor"])
def update_actor(id:int,actor:Actor):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"actor dont't found", "status_code":404})
    ActorService(db).update_actor(actor)
    return JSONResponse(content={"message":"actor update succeefully","status_code":202}, status_code=202)
    
    #todo editar
    
@actor_router.delete("/actor{id}",tags=["actor"])
def delete_actor(id:int,movie:Actor):
    db = Session()
    result = ActorService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"actor dont't found", "status_code":404})
    ActorService(db).delete_actor(id)
    return JSONResponse(content={"message":"actor delete successfully", "status_code":200}, status_code=200)




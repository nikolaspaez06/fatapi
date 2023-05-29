from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse

genres_router = APIRouter()


@genres_router.get("/genres",tags= ['genres'], status_code=200)
def get_genres():
    """function to check the route"""
    return HTMLResponse("<h1>Hello desde ruta de genres</h1>")

@genres_router.get('/genres',tags= ['genres'], status_code=200)
def get_genres():
    #fincion que trae todos los generos que esta en servicio 
    return JSONResponse(content={'message': 'esto son los generos'})

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres():
    #llamar funcion que va a estar en el servidor 
    return JSONResponse(conten={"message":"genre create successfully"})


#creamos un get que trae un solo genero por id 
@genres_router.get('/genres/{genres_id}', tags=['genres'], status_code=200)
def get_genres(genres_id: int):
    genre = genrens_router.get_genre(genres_id)
    return genre
# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos


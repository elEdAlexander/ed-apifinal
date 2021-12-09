from typing import List
from pydantic import BaseModel

class pelicula(BaseModel):
    id:int
    nombre:str
    fecha:str
    comentario:str
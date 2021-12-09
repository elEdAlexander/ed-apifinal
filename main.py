from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from modelos import *
import database

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"Mensaje":"Proyecto final"}

@app.post("/peliculas/agregar", tags=['Peliculas'])
def agregar_peliculas(peli:pelicula):
    database.guardarpelicula(peli)
    return {"Msg":"La pelicula fue guardada"}

@app.put("/peliculas/actualizar", tags=['Peliculas'])
def actualizar_peliculas(peli:pelicula):
    database.actualizarpelicula(peli)
    return {"Msg":"La pelicula fue actualizada"}

@app.get("/peliculas/lista", tags=['Peliculas'])
def lista_peliculas():
    tmp = database.cargarpeliculas()
    return tmp

@app.delete("/peliculas/eliminar", tags=['Peliculas'])
def eliminar_peliculas(num:int):
    database.eliminarpelicula(num)
    return {"Msg":"La pelicula fue Eliminada"}

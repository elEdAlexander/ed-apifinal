from re import template
from peewee import *
from modelos import *

db = SqliteDatabase('dbfinal.db')


class pelicula(Model):
    nombre = CharField()
    fecha = CharField()
    comentario = CharField()

    class Meta:
        database = db

db.connect()

db.create_tables([pelicula])


def guardarpelicula(obj:pelicula):
    peli = pelicula()
    peli.nombre = obj.nombre
    peli.fecha = obj.fecha
    peli.comentario = obj.comentario
    peli.save()

def cargarpeliculas():
    peliculas = []
    for peli in pelicula.select().dicts():
        peliculas.append(peli)
    return peliculas

def actualizarpelicula(obj:pelicula):
    peli = pelicula.get(pelicula.id == obj.id)
    peli.nombre = obj.nombre
    peli.fecha = obj.fecha
    peli.comentario = obj.comentario
    peli.save()

def eliminarpelicula(peli):
    user = pelicula.get(pelicula.id == peli)
    user.delete_instance() 
        
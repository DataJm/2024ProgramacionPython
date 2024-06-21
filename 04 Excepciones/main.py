'''
Crear reporte de "buenos shows" de Netflix

TODO:
- Pedir al usuario un rating
- Buscar en el archivo CSV de Netflix todos los show con rating igual
o mayor al buscado por el usuario
- Vamos a crear el archivo CSV con todos los shows de la busqueda

'''

import os

from modulos.funciones import get_user_rating, filtrar_shows, guardar_shows 

csv_path = os.path.join('..', 'datos', '01netflix.csv')

rating = get_user_rating()

shows_filtrados = filtrar_shows(rating, csv_path)

csv_new_file = os.path.join('.', 'shows.csv')

guardar_shows(shows_filtrados, csv_new_file)
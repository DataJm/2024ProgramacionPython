'''
TODO:

Escribe un programa (de preferencia modularizado) que le pida al usuario un modelo de la marca
"Audi" (A1, A3, R8, etc) y muestra en pantalla cuántos autos tenemos en inventario de
ese modelo y crea un nuevo archivo CSV con todos los autos de ese modelo particular.

TODO:

- Genera más estadística del modelo elegido:
    - Máximo, Mínimo, Promedio del precio
    - Cuántos a Gasolina y cuántos a Diesel

- Envía los resultados a SQL

'''

import os

from modules.utils import get_user_model, filter_data, get_kpis, save_data, get_kpis_v2

csv_path = os.path.join('..', 'datos', '03audi.csv')

user_model = get_user_model()

filtered_data = filter_data(user_model, csv_path)

get_kpis_v2(user_model, filtered_data)

csv_new_file = os.path.join('.', 'filtered_data.csv')

save_data(filtered_data, csv_new_file)
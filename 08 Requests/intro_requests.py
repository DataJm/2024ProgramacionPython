'''
Automatizar descarga de HTML, XML
'''

import requests
url = "https://books.toscrape.com/"
respuesta = requests.get(url)

# Con esto vemos el código de la petición
# print(respuesta)
# Con esto vemos el código que recibió la petición
# print(respuesta.text)

# Si te interesa hacer mineria de texto (web scraping)
# para extraer información puedes usar: 
# En resumen: 
# BeautifulSoup entiende el código HTML y XML,
# por lo tanto, para extraer información de esos formatos
# nos conviene usar este paquete
# https://www.crummy.com/software/BeautifulSoup/

# Preguntas:
# Es posible envíar información (no solo recibir )?  Si, por ejemplo el método HTTP "post" envía información
# requests.post()
# También es posible envíar información utilizando un "robot" (navegador web) controlado por Python
# Librería recomendada : 
# https://selenium-python.readthedocs.io/installation.html#introduction
# Libro:
# Web Scraping with Python: Collecting More Data from the Modern Web
# https://www.amazon.com.mx/Web-Scraping-Python-Collecting-Modern


'''
Automatizar descarga desde un JSON
Modificaremos el código para consumir data de una API
'''

# URL de la API (endpoint)
url = "https://api.spacexdata.com/v3/capsules"

# Estoy haciendo en dos pasos: la petición y transformar la respuesta de JSON a Python
# respuesta = requests.get(url)
# respuesta = respuesta.json()

# Típicamente lo hacemos en un único paso:
respuesta = requests.get(url).json()
# El método JSON convierte el JSON en una estructura de datos de Python
# (lista o diccionario)

# Usamos la funcíon type para saber si es lista o diccionario:
print(type(respuesta))

# En este caso en particular tengo una lista
# por lo tanto puedo hacer todo lo que
# sobre listas.
print(respuesta[0]["capsule_serial"])

# Por ejemplo:
# Extraer el "capsule_serial"
# de todos los objetos
lista_nueva = []
for x in respuesta:
    lista_nueva.append(x["capsule_serial"])

print(lista_nueva)

# Se puede poner MUY complejo
# Vamos a guardar todas las "misiones"
# en el JSON
lista_misiones = []
for capsule in respuesta:
    misiones = capsule["missions"]
    for mision in misiones:
        lista_misiones.append(mision["name"])

print(lista_misiones)



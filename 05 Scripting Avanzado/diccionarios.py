'''
Diccionarios

Son estructuras de datos de llave - valor (pair wise)
Son de las estructuras más importantes en Python

e.g. En el estudio de algoritmos, los árboles de ordenamiento se hacen con diccionarios
e.g. Los diccionarios son muy similares a los JSON de JavaScript

Nota: También se le llama datos semi-estructurados

'''

'''
No tienen orden, su índice es la llave y son mutables
'''
actor = {
    "nombre": "Sly",
    "edad" : 78,
    "profesion" : "Actor",
    "retirado": True,
    "peliculas": ["rocky","rambo","tango y cash","asesinos"],
    "premios":{
        "globos de oro": [2015],
        "otros": [2015,1997]
    }
}

# Cómo acceder a los datos de un diccionario ? 
print(actor)
print(actor["nombre"].split('l'))
print(actor["edad"] / 10)
print(actor["peliculas"][-1])
print(actor["premios"]["globos de oro"][0])

# Agregar información a la lista de peliculas
actor["peliculas"].append("Cobra")

# Agregar nuevas llaves
actor["Pareja"] = "Angie"

print(actor)

import pprint
print("------------------")
pprint.pp(actor)

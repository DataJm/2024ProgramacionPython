# print("hola")
# print("jose")
# print("buen")
# print("dia")

nombre = "jose"

print(f"""
    Hola
    {nombre}
    buen
    dia
      """)

"""
Introducción a funciones:
Vamos a ver la lógica de las funciones
en python, veremos unas cuantas
funciones básicas.
"""

# int()
print("Función int")

valor = "10"
print(valor*10)

valor = int(valor)
print(valor*10)

print(f'''
{"#"*50}
Ejemplo de mensaje importante      
''')

valor = int(3.99)
print(valor)

'''
La función float() también
te convierte un string a número,
pero además te respeta los decimales
'''

valor_flotante = float("10")
valor_flotante = float(3.1416)

'''
ESTRUCTURAS DE DATOS

Listas

La lista en python es una colección de ítems
que :
- Es ordenada
- Es indexada
- Es mutable
- Puede tener cualquier tamaño y cualquier tipo de dato
'''

print(f'''
{"#"*50}
Listas
''')

mi_lista = ["jose","alejandra","claudia","carlos"]

# Acceder a los elementos de una lista
print(mi_lista[3])

'''
Python es un lenguaje de programación orientado
a objetos. En python TODO es un objeto.

La consecuencia de esto, los objetos tienen métodos 
y propiedades. Donde los métodos son "funciones que viven
dentro del objeto"
'''

# Método "append"
# El método append agrega un item a la lista
mi_lista.append("Daysi")

print(mi_lista)

# Método "pop"
# Elmina el último item de la lista
mi_lista.pop()
print(mi_lista)

# Método "reverse"
# Invierte los elementos de la lista
mi_lista.reverse()
print(mi_lista)

mi_lista[1] = 100
print(mi_lista)

print(f'''
{"#"*50}
Tuplas
''')

'''
Tuplas

La tupla, es una colección de items,
puede tener cualquier número de ítems, 
cualquier tipo de item
- Ordenada
- Indexada
- INMUTABLE
'''

mi_tupla = (18,40,35,20, 20 )

# Acceder a los elementos
print(mi_tupla[0])

# NO PODEMOS MODIFICAR LA TUPLA
# mi_tupla[0] = 999

# Método count()
# Cuántas ocurrencias hay del item que pasamos
# al método
print(mi_tupla.count(20))

'''
MODULOS

En python los modulos (librerias) son colecciones
de funciones creadas por "la comunidad".

Es bastante común tener que auxiliarnos
en estos modulos para construir nuestros programas.

'''

print(f'''
{"#"*50}
Random
''')

# Modulo random para la creación
# de números aleatorios
import random

# Método random()
# Crea un número aleatorio entre 0 y 1
aleatorio = random.random()
print(aleatorio)

# Método randint()
# Crea un número aleatorio (Entero)
# entre un rango determinado
aleatorio = random.randint(0,100)
print(aleatorio)

# Método choice()
# Elige un item de manera aleatoria
# de una colección de ítems

item_aleatorio = random.choice(mi_lista)
print(item_aleatorio)
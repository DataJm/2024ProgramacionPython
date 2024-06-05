'''
Ciclos / Bucles

Una de las principales razones para usar python es la repetición / automatización de tareas.
Un bucle significa repetir un bloque de código "n" veces.
Veremos las opciones que tenemos para repetir pasos en python

'''

# While
# El bloque de código se repetirá mientras la condición a evaluar sea verdadera

n = 0

while n<5:
    print(f'Valor de n : {n}')
    n = n + 1
    # La palabra reservada 'break' termina el
    # bucle y sale
    # break

print('Fin del while')

# For
# Iteramos sobre un iterable

# Una coleccion de items es iterable
mi_lista = ['a','b','c','d']

for x in mi_lista:
    print(f'{x}')

print('Fin de ciclo for')

# Los string tambien son iterables

for a in 'mensaje':
    print(a)

# Los 'range' son rangos de numeros iterables

for x in range(15):
    print(x)

# Cuantos elementos tiene una lista/ tupla ?
print(len(mi_lista))

'''
TODO:
Crea una lista con nombres de personas
Crea una tupla con las edades de esas personas

Crea un ciclo for para imprimir en pantalla
a cada persona con su edad

- Crea la lista y la tupla
- Haz un ciclo for con un range de "n" items
- Utiliza el valor de "x" para acceder a los items
- Imprime en pantalla nombre y edad

'''

nombres = ["a","b","c","d","e"]
edades  = [20,18,30,29,40]

for i in range(len(nombres)):
    print(f'Nombre: {nombres[i]}, Edad: {edades[i]}')


# Primera iteración
for i in range(10):
    print("Valor de i", i)
    for t in range(3):
        print("Valor de t", t)
        if t==3:
            print("Valor de t es 3")

print("fin del doble for")



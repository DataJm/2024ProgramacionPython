'''
List comprehension

Es una forma de crear listas a partir de iterables
en una sola línea de código
'''

scores = [9,8,7,5,9,10]

# TODO: Multiplicar cada score por 10, guardar el resultado en una lista

resultado = []

for x in scores:
    resultado.append(x*10)

print(resultado)

# List comprehension
# nueva_lista = [return for iterador in iterable]

resultado = [x*10 for x in scores]
print(resultado)

# TODO: A partir de una lista de temperaturas en C,
# crea una nueva lista con las temperaturas en F

temps = [ 24, 29, 30, 45]

temps_f = [(9/5) * c + 32 for c in temps ]

print(temps_f)


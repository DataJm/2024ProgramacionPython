# archivo = open('../datos/01netflix.csv', 'r')

# print(next(archivo))

# print(next(archivo))

# print(next(archivo))

# for linea in archivo:
#     print(linea)

with open('../datos/01netflix.csv', 'r') as archivo:
    for linea in archivo:
        # Cada línea es un string
        # print(type(linea))
        datos = linea.split(',')
        print(datos[0], datos[5])

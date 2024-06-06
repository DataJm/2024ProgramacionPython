'''
Escribe un programa que le pide un show
al usuario, lo busca en el CSV de Netflix
y muestra en pantalla el nombre del show,
su clasificación, y su user rating score
'''

user_input = input("Que show deseas ver ?")

with open('../datos/01netflix.csv', 'r') as archivo:
    for linea in archivo:
        datos = linea.split(',')
        show = datos[0]
        rating = datos[5]
        if show == user_input:
            print(show, rating)
            break


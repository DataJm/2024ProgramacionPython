#archivo = open('salida.txt','w')

#archivo.write('hola mundo')

#archivo.close()

# Permisos de escritura ( sobre escribe) con w
with open('salida.txt','w') as archivo:
    archivo.write('Primera linea')

# Permisos de Append ( agregar) con a
with open('salida.txt','a') as archivo:
    archivo.write('\nnueva linea')


# Actividad
# TODO: 
# Genera un archivo con los nombres de estudiantes
# donde los nombres están guardados en una lista

alumnos = ['jose','erick','alejandra','israel','claudia']

with open('alumnos.txt', 'w') as archivo:
    for alumno in alumnos:
        archivo.write(alumno+'\n')

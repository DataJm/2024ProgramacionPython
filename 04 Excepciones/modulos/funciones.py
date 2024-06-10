import csv

def get_user_rating():
    rating = input('Rating para buscar shows mayor o igual a: ')
    
    # Opcion 1 (no funciona):
    # Verificar que el string tiene digitos
    # Esto en realidad no me funciona :/ 
    # if rating.isdigit():
    #     rating = float(rating)
    #     return rating
    # else:
    #     raise Exception('Por favor, dame un número')

    # Opcion 2: Try /Except
    # Es como un "if", donde tenemos un bloque de código
    # que "intentaremos" ejecutar, y en caso de tener error
    # se va al Except
    try:
        # Python intentará correr este código
        rating = float(rating)
        return rating
    except Exception as err:
        # En caso de gerar error en el bloque de try
        # correra este código
        print("""
              

        Por favor, debes envíar un número
        Usaré el valor default de 0

        """)
        # La palabra reservada "raise" es opcional
        # sirve para detener el programa
        # y mandar el error a consola
        # print(err)
        # raise

        # Opcional, podemos solo invocar "exit" para
        # detener el programa
        # exit()
        return 0
    
def filtrar_shows(rating, archivo):
    with open(archivo) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        resultados = []

        for row in csv_reader:
            try:
                show_rating = float(row[-2])
                if show_rating>=rating:
                    # print(row[0])
                    resultados.append(row)
            except:
                # print(f'Saltando: {row[0]}')
                next
    return resultados

def guardar_shows(resultados, archivo):
    """
    Guarda los resultados en un archivo CSV.

    Args:
        resultados (list): Lista de filas a guardar.
        archivo (str): Ruta al archivo CSV de salida.

    Returns:
        None
    """
    with open(archivo, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in resultados:
            csv_writer.writerow(row)
    print(f'Resultados guardados en: {archivo}')

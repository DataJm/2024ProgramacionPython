import csv
import pprint

def get_user_model():
    user_model = input('Por favor ingresa el modelo que te interesa: ')
    return user_model
    
def filter_data(user_model, csv_path):
    with open(csv_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        # results = []

        # for row in csv_reader:
        #     if row[0]==user_model:
        #         results.append(row)
        results = [row for row in csv_reader if row[0]==user_model]

    return results

def save_data(filtered_data, csv_new_file):

    with open(csv_new_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in filtered_data:
            csv_writer.writerow(row)
    print(f'Resultados guardados en: {csv_new_file}')


def get_kpis(user_model, filtered_data):

    kpis = {
        "conteo"      : 0 ,
        "mínimo"      : 999999 ,
        "máximo"      : 0 ,
        "suma_precio" : 0
    }

    for row in filtered_data:
        # DRY / Dont Repeat yourself
        precio = float(row[2])
        
        kpis["conteo"] += 1
        kpis["suma_precio"] += precio
    
        if precio<kpis["mínimo"]:
            kpis["mínimo"] = precio

        if precio>kpis["máximo"]:
            kpis["máximo"] = precio

    kpis["promedio"] = kpis["suma_precio"] / kpis["conteo"]

    print(f'''
    Indicadores del modelo : {user_model}
    ''')
    # Opcion 1
    pprint.pp(kpis)

    # Opcion 2
    for llave, valor in kpis.items():
        print(f'{llave} : ')


def get_kpis_v2(user_model, filtered_data):
    

    kpis = {
        "conteo"      : 0 ,
        "mínimo"      : 999999 ,
        "máximo"      : 0 ,
        "suma_precio" : 0
    }

    # Extraer los precios de todos los autos
    lista_precios = [float(row[2]) for row in filtered_data]

    kpis["máximo"] = max(lista_precios)
    kpis["mínimo"] = min(lista_precios)
    kpis["suma_precio"] = sum(lista_precios)
    kpis["conteo"] = len(lista_precios)
    kpis["promedio"] = kpis["suma_precio"] / kpis["conteo"]

    print('Resultados: ' + user_model)
    pprint.pp(kpis)
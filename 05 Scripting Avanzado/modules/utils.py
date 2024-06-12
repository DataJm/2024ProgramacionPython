import csv

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
    # Conteo
    conteo = 0
    for x in filtered_data:
        conteo += 1
    
    print(f'''
    Indicadores del modelo : {user_model}
    En total tenemos {conteo} autos
    ''')
fecha_inicial = input('Dame una fehca de inicio')
fecha_final = input('Dame una fehca de fin')


query = f'''
SELECT FROM table
WHERE fecha in between {fecha_inicial} and {fecha_final}
'''
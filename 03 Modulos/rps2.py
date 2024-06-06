import random
'''
Capturar el input del usuario,
y generar el arma elegida por ambos jugadores
'''
armas = ['piedra','papel','tijera']
'''
Varieble para controlar la continuadad del juego
'''
continuar = True
resultados = []
while continuar:
    arma_computadora = random.choice(armas)
    user_input = input('(0)Piedra, (1)Papel, (2)Tijeras')
    # TODO: Verificar que el usuario colocó un número válido
    user_index = int(user_input)
    arma_usuario = armas[user_index]
    '''
    Condicionales
    '''
    if arma_computadora==arma_usuario:
        resultado = 'Empate'
    else:
        # TODO: Crear los escenarios del juego
        resultado = 'Combate'
    
    print(resultado)
    resultados.append(resultado)
    '''
    Preguntar al usuario si desea volver a jugar
    '''
    user_input_continue = input('(0)Continuar, (1)Finalizar')
    if user_input_continue!='0':
        continuar = False

'''
Guardar resultados de todos los juegos
'''
with open('resultados.txt', 'w') as archivo:
    for resultado in resultados:
        archivo.write(resultado+'\n')

    #archivo.writelines(resultados)


import random

'''
TODO:
Crear un programa para jugar Piedra, Papel o Tijera
contra la computadora

- Mensaje de bienvenida
- Pedirle un input al usuario (recomiendo que sea un número)
- Elegir aleatoriamente un arma para la computadora (import random)
- Escribir el "if else" para los escenarios
- Mensaje con el resultado del combate

'''

'''
TODO:
- El juego se puede repetir todas las veces que el usuario lo desee
- Guardar los resultados de todos los juegos que se han estado jugando
- Guardar los resultados en un archivo .txt
'''

print(f'''
{"-"*50}
Piedra papel o Tijera
{"-"*50}

''')

choices = ["rock","paper","scissors"]

computerChoice = random.choice(choices)

humanChoice = input("Elige tu arma: piedra(0), papel(1), tijera(2)")
humanChoice = int(humanChoice)
humanChoice = choices[humanChoice]

print(f'''
Computadora: {computerChoice}
Humano     : {humanChoice}
''')

if(computerChoice==humanChoice):
    print(" \n  OMG IT'S A TIE!")
# rock and paper
elif(computerChoice=="rock" and humanChoice=="paper"):
    print("paper > rock \n  YOU WON, HUMAN WINS!")
elif(computerChoice=="paper" and humanChoice=="rock"):
    print("paper > rock \n  YOU LOSE, COMPUTER WINS!")
# rock and scissors
elif(computerChoice=="rock" and humanChoice=="scissors"):
    print("rock > scissors \n  YOU LOSE, COMPUTER WINS!")
elif(computerChoice=="scissors" and humanChoice=="rock"):
    print("rock > scissors \n  YOU WON, HUMAN WINS!")
# paper and scissors
elif(computerChoice=="paper" and humanChoice=="scissors"):
    print("scissors > paper \n  YOU WON, HUMAN WINS!")
elif(computerChoice=="scissors" and humanChoice=="paper"):
    print("scissors > paper \n  YOU LOSE, COMPUTER WINS!")
else:
    print("ERROR                  ############################################################################################")
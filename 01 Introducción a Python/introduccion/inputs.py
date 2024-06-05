# TODO: Escribe un programa que reciba 2 números del usuario
# y realice las operaciones de: suma, resta, multiplicación
# y división). Muestra los resultados en pantalla en un 
# formato amigable.
# Crea un if para imprimir en pantalla cuál de los dos
# números es el mayor

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

if numero1>numero2:
    print('Numero 1 es mayor')
elif numero2>numero1:
    print('Numero 2 es mayor')
else:
    print('Son el mismo numero')
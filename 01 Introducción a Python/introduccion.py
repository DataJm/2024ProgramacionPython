# Tipos de variables en python
# String
nombre = "jose manuel"
# Entero
edad = 37
# Booleano
programador = True
# Float
peso = 89.5

# Operadores aritméticos
# +
# *
# -
# / 
# %

print("Operaciones")
print(2+2)
print(2*8)
print(25/3)
print(5%2)
print(2**4)

# Operador +
# También funciona para concatenar
a = "Hola"
b = "Mundo"
print(a+b)

# print("a" + 2)
print(str(2)+ "a")

# f-strings
# Muy recomendados, son templates

print(f"Mi edad es {edad}")

# Operadores lógicos

a = 5>2 # True
b = 10>1 # True

print(a and b) # True

# Or: Una condición debe ser True
# En cuanto python encuentra un true,
# hace return del true e ignora lo demás
print(True or 2+'a') # True

print(not True)

# Comparación
print(5==5) # True
print(5!=5) # False

# Condicionales
# if

x = 10

if x > 1 :
    print(f'{x} es mayor que uno')
else:
    print(f'{x} no es mayor que uno')

x = 10
y = 10

if x>y:
    print('Escenario 1')
elif y>x:
    print('Escenario 2')
elif x==y:
    print('X es igual a y')
else:
    print('No se que es X y Y')
    raise Exception("Oh no")














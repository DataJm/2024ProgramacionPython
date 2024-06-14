
'''
Crear objetos en Python
'''

class Dog():
    # Codigo independiente de funciones
    def __init__(self, nombre, color):
        print("Se ha instanciado un nuevo Dog")
        self.name = nombre
        self.color = color

    def saludar(self):
        print("Hola")

perrito1 = Dog('firulais','cafe')
perrito2 = Dog('perefjil','verde')

print(perrito1.name)
print(perrito2.color)

perrito1.saludar()
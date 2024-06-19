import tkinter as tk

# Iniciamos una nueva aplicación
root = tk.Tk()
# Agregamos un título a la ventana principal
root.title("Hola Mundo")
# Modificar el tamaño de la ventana principal
root.geometry('400x400')

# Crearemos una etiqueta
etiqueta = tk.Label(root, text="Esta es mi etiqueta")
# Mostrar la etiqueta
# El comportamiento default es: secuencial y centrado
etiqueta.pack()

# Creamos 3 etiquetas
# https://docs.python.org/es/3.10/library/tkinter.ttk.html#label-options
etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="red")
etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="green")
etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="blue")

# https://docs.python.org/es/3/library/tkinter.html
etiqueta1.pack(side='top')
etiqueta2.pack(side='left')
etiqueta3.pack(side='right', expand=1, fill='y')
root.mainloop()
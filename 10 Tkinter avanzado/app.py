import tkinter as tk

def mostrar_mensaje():
    texto = entrada.get()
    # print(texto)
    label = tk.Label(root, text=texto)
    label.grid(row=2,column=0)

root = tk.Tk()
root.title('App de Tkinter')
root.geometry('400x400')

entrada = tk.Entry(root)

# entrada.pack()
etiqueta = tk.Label(root, text="Escribe tu comentario        ")
etiqueta.grid(row=0,column=0)
entrada.grid(row=0,column=1)

button = tk.Button(root, text="Guardar", width=15, command=mostrar_mensaje)
button.grid(row=1, column=1)

listbox = tk.Listbox(root)
listbox.grid(row=3, column=0)

for i in range(5):
    listbox.insert(tk.END, f'Elemento {i}')

root.mainloop()



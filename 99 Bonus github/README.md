# demo_github

Comandos de git:

Clonar el repositorio
$ git clone URL

Revisar los cambios en el repositorio
$ git status

Añadir cambios al repositorio
$ git add

No es necesario, pero si volvermos a hacer "git status"
podremos ver los cambios agregados al repositorio
$ git status

Todos los cambios que mandemos al repositorio
tienen que venir acompañados de un mensaje.
Ese mensaje se espera que sea explicativo sobre
los cambios realizados.

Existe documentación y buenas prácticas sobre estos mensajes,
lo más sencillo es usar la siguiente notacion: "accion: comentario"
"dev: nueva funcion"
"bug: corregi error en script.py"
"dev: agregue documentacion de la funcion main"

$ git commit -m 'dev: desarrollo de primer codigo'

Ahora si estamos listos para subir todos los cambios al repositorio
$ git push

# Entornos virtuales de python

Son sandbox que nos ayudan a controlar las dependencias de un proyecto de Python

#### Crear un entorno virtual llamado 'demo'
`python -m venv demo`

Una vez que creamos el entorno virtual, ahora necesitamos activarlo
(es decir, dejar de trabajar con nuestro 'Python global' y empezar
a trabajar con el Python local que acabamos de crear para este proyecto)

#### En windows, Mac, Linux
`source demo/Scripts/activate`

#### Verificar los paquetes instalados con pip
`pip list`

A partir de este momento ya tengo una version de python dedicada a mi proyecto.
Puedo instalar las dependencias con :
`pip install sqlalchemy`

Y para generar el archivo con todas las dependencias:
`pip freeze > requirements.txt`

# CUIDADO
Definitivamente NO QUEREMOS subir a nuestro repositorio
toda una copia de Python (la carpeta demo).

Asi que vamos a agregarla a `.gitignore`

.gitignore
`demo/`

### Del lado del servidor solo necesitas:

- Instalar Python
- Usar `pip install requirements.txt`

Con eso ya puede correr tu proyecto

##### Como hacer que ejecute cada 24 horas?
Depende del sistema operativo, con un cronjob es suficiente




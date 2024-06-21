'''
Envíar información vía URL

Se llama "query url" cuando envíamos variables
vía http.get (en la url) hacia el servidor

NOTAR QUE ESTO PUEDE INCURRIR EN UNA INSEGURIDAD
no es terrible, hay soluciones adicionales
(simplemente no pasarle a nadie tu llave)
pero si tenemos que ser concientes que ocurre

'''
import requests

url = "https://www.omdbapi.com/?i=tt3896198&apikey=XXXX"
respuesta = requests.get(url).json()
print(respuesta)
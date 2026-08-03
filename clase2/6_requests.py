import requests

url = "https://jsonplaceholder.typicode.com/posts"
respuesta = requests.get(url)
datos = respuesta.json()
# print(datos)
print(len(datos))
print(type(datos))

print(datos[0]["title"])

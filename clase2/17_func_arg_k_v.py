def saludar(**kwargs) -> None:
    nombre = kwargs.get("nombre", "Anónimo")
    edad = kwargs.get("edad", "desconocida")
    altura = kwargs.get("altura", "desconocida")
    activo = kwargs.get("activo", False)
    print(
        f"Hola, {nombre}! Tienes {edad} años. Tu altura es {altura} y estás {'activo' if activo else 'inactivo'}."
    )


saludar(nombre="Maria", edad=25)
saludar(nombre="Juan", edad=25, altura=1.75, activo=True)
saludar(**{"nombre": "Pedro", "edad": 30, "altura": 1.80, "activo": False})

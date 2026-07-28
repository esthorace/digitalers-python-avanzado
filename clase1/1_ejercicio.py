"""
A partir de dos variables llamadas nombre y edad:
crear una variable que almacene si se cumplen las siguientes condiciones,
y mostrar al usuario True o False:
    - nombre sea diferente de cuatro asteriscos ****
    - edad sea mayor que 5 y a su vez menor que 20
    - Que la longitud de nombre sea mayor o igual a 4 pero a la vez menor que 8
    - edad multiplicada por 3 sea mayor que 35

No debes usar funciones, ni condicionales (if), bucles (while-for) o cualquier
otra instrucción que no hayamos visto.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

validacion_nombre = nombre != "****"
validacion_edad = edad > 5 and edad < 20
validacion_nombre_longitud = len(nombre) >= 4 and len(nombre) < 8
validacion_edad_calculada = edad * 3 > 35

# validacion = (
#     validacion_nombre
#     and validacion_edad
#     and validacion_nombre_longitud
#     and validacion_edad_calculada
# )

validacion = all(
    [
        validacion_nombre,
        validacion_edad,
        validacion_nombre_longitud,
        validacion_edad_calculada,
    ]
)

print(validacion)

"""
-- Objetivo: Empacar y desempacar

Crear una tupla que represente un cajón de verduras
Crear otra tupla que represente un cajón de frutas
Crear una tupla llamada camion, que contenga los dos cajones anteriores
Mostrar los datos
"""

cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")

# Carga de camión 1
camion_1 = (cajon_verduras, cajon_frutas)
print(camion_1)

# Descargar del camión 1
verduras, frutas = camion_1
print("Cajón de verduras:", verduras)
print("Cajón de frutas:", frutas)

# Cargar en el camión 2
camion_2 = cajon_verduras + cajon_frutas
print("Camion 2:", camion_2)

# Carga de camión 3
camion_3 = (*cajon_verduras, *cajon_frutas)
print("Camion 3:", camion_3)

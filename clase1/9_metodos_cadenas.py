que_es_python = " pithon es un lenguaje de programación interpretado  "


# upper() convierte la cadena a mayúsculas
print("upper():", que_es_python.upper())
# lower() convierte la cadena a minúsculas
print("lower():", que_es_python.lower())
# title() convierte la primera letra de cada palabra en mayúscula
print("title():", que_es_python.title())
# capitalize() convierte la primera letra de la cadena en mayúscula
# strip() elimina los espacios en blanco al inicio y al final de la cadena
print("capitalize() y strip():", que_es_python.strip().capitalize())

# count() cuenta la cantidad de veces que aparece un carácter en la cadena
print("count():", que_es_python.count("o"))

# isdecimal() verifica si la cadena es un número decimal
print("isdecimal():", "12345".isdecimal())
print("isdecimal():", "a12345".isdecimal())

# isalpha() verifica si la cadena es un alfabeto
print("isalpha():", "abc".isalpha())
print("isalpha():", "a12345".isalpha())

que_es_python = " pithon es un lenguaje de programación interpretado  "
# replace() reemplaza una parte de la cadena por otra
print("replace():", que_es_python.replace("e", "3"))

# split() divide la cadena en una lista
print("split():", que_es_python.split("programación"))

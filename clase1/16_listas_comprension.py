numeros = [1, 2, 3, 4, 5, 6]


# numeros_pares = []
# for n in numeros:
#     if n % 2 == 0:
#         numeros_pares += [n]

numeros_pares = [n for n in numeros if n % 2 == 0]

print(numeros_pares)

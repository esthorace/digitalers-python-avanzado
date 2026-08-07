def funcion(argumento, argumento2, *args, **kwargs):
    print("argumento: ", argumento)
    print("argumento2: ", argumento2)
    print("args: ", args)
    print("kwargs: ", kwargs)


datos = {"username": "juan123", "password": "123456"}

funcion(
    "hola",
    1,
    2,
    3,
    4,
    [True, False],
    idioma="español",
    nacionalidad="argentino",
    **datos,
)

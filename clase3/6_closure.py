def contador():
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return incrementar


c = contador()  # c es una función que incrementa la cuenta
print(c())  # 1
print(c())  # 2
print(c())  # 3

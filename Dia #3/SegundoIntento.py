def num_descompose(x):
    return [10]* (x // 10) + [5] * ((x % 10) // 5) + [1] * ((x % 10) % 5)

numero = int(input(""))
print(num_descompose(numero))



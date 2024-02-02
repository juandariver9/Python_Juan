#Dia 1

#Sin parametros y sin retorno
def SinSin():
    print("Hola Mundo!")


#Sin parametros y con retorno
def SinCon():
    c = 3 + 5
    return c


#Con Parametors y sin retorno
def ConSin(a, b):
    c = a + b
    print("La suma es: ", c)


#Con Parametros y Con retorno
def ConCon(x,y):
    n = x / y
    return round(n,2) #round es pa redondear dahh, y el 2 es para cuantos decimales se dejan

#Dia 2

def Secuencia(n):
    Fib = [0, 1]
    for i in range(2, n):
        Fib.append(Fib[i - 1] + Fib[i - 2])
    return Fib

#Dia 3
def num_descompose(x):
    return [10]* (x // 10) + [5] * ((x % 10) // 5) + [1] * ((x % 10) % 5)

#Dia 4
def encontrar_pares_divisibles(lista, k):
    pares_divisibles = set()

    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if (lista[i] + lista[j]) % k == 0:
                pares_divisibles.add((lista[i], lista[j]))

    return pares_divisibles

import itertools

def encontrar_pares(n, k, A):
    pares = []  # Lista para almacenar los pares encontrados
    for i, j in itertools.combinations(range(n), 2): #Lo que dijo Helen
        # Verificar si la suma de los elementos en los índices i y j es divisible por k
        if (A[i] + A[j]) % k == 0: 
            # Crear un par ordenado y asegurarse de que no esté duplicado en la lista
            par = tuple(sorted((A[i], A[j])))
            if par not in pares:
                pares.append(par)
    return pares
import math
def Colision(bola1, bola2):
    x1, y1, z1 ,r1 = bola1
    x2, y2, z2 ,r2 = bola2

    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) + (z2 - z1)**2
    print(distance_euclides)

    return distance_euclides <= r1 + r2

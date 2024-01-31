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

T = int(input("Ingrese el número de casos de prueba: "))
for t in range(T):
    # Leer el tamaño de la lista y el valor por el cual la suma debe ser divisible
    n, k = map(int, input("Ingrese n y k: ").split())
    
    # Leer la lista de enteros
    A = list(map(int, input("Ingrese la lista de enteros A: ").split()))
    
    # Llamar a la función encontrar_pares con los parámetros dados
    pares = encontrar_pares(n, k, A)
    
    # Imprimir el número de pares encontrados para el caso de prueba actual
    print("Caso", t+1, ":", len(pares))
    
    # Imprimir cada par encontrado en el formato especificado
    for par in pares:
        print("(", par[0], ",", par[1], ")", sep="", end=" ")
    print()

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
#Muestra los pares de listas y quita los duplicados
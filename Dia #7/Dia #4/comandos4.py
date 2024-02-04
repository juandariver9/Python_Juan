def Monedeas():
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
    Casos = []
    lista_separada = []
    lista_separada_numeros = []
    T = int(input("T: "))
    for t in range(T):
        # Leer el tamaño de la lista y el valor por el cual la suma debe ser divisible
        nk = str(input(" "))
        lista_separada = nk.split(" ")
        caracteres_lista = len(lista_separada)
        lista_separada[-1] = int(lista_separada[-1])
        n = lista_separada[0]
        n = int(n)
        k = lista_separada[1]
        k = int(k)

        A = list(map(int, input(" ").split()))
    
        # Llamar a la función encontrar_pares con los parámetros dados
        pares = encontrar_pares(n, k, A)
    
        # Imprimir el número de pares encontrados para el caso de prueba actual
        Casos.append(len(pares))
    for z in range(0,T,1):
        print(f"Caso #{z+1}: ",Casos[z])


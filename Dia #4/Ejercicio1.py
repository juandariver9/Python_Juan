def Repeticion(n):
    x = math.factorial(n+2-1)
    y = math.factorial(2) * math.factorial(n-1)
    CantidadRepeticiones = x / y
    return CantidadRepeticiones


import math

T = int(input("CASOS: "))

almacen = list([])
Conjunto = {}
for i in range(0,T,1):
    nk = str(input(f"n numeros y k de caso #{i+1} "))
    lista_separada = nk.split(" ")
    caracteres_lista = len(lista_separada)
    #print(caracteres_lista) # Quitar luego
    #print(lista_separada) # Quitar luego
    lista_separada[-1] = int(lista_separada[-1])
    n = lista_separada[0] # Separar n de la lista nk
    n = int(n)
    #print(n)
    k = lista_separada[1] # Separar k de la lista nk
    #print(k)
    k = int(k)
    for j in range(0,caracteres_lista-1,1):
        numero = int(lista_separada[j])
        lista_separada[j] = numero
    #print(lista_separada) # (0, 1) 0 = n numeros 1 = k
    for l in range(0,lista_separada[0],1):
        numeros = int(input(f"#{l+1}: "))
        almacen.insert(0,int(math.fabs(numeros)))
        print(almacen) # Quitar luego
    #Separar listas en elementos de a 2
def ejercicio1():
    Tabla = {
        "Productos": ("Manzana", "Computador", "Hacienda", "Celular"),
        "Precios": (2500, 200, 250000000, 300000)
    }

    print("PRODUCTOS \tPRECIOS")
    for i in range(4):
        print(Tabla["Productos"][i], "\t", Tabla["Precios"][i])

    Producto = str(input("Digite el producto que desea: "))
    Producto = Producto.capitalize()

    if Producto in Tabla["Productos"]:
        Cantidad = int(input(f"Digite la cantidad de {Producto.lower()}s que desea: "))
        indice_producto = Tabla["Productos"].index(Producto)
        PrecioTotal = Tabla["Precios"][indice_producto] * Cantidad
        print(f"El precio total de {Cantidad} {Producto.lower()}s es: {PrecioTotal}")
    else:
        print(f"Lo siento, el producto {Producto} no está en la tabla.")

def ejercicio2():
    def negate(num):
        return -num

    def large_num(num):
        res = (num > 1000)
        return res  

    b = 1200  

    neg_b = negate(b)  
    print('b:', b, 'neg_b:', neg_b)  

    big = large_num(b)
    print('b is big:', big)
    
    
def ejercicio3():
    
    print("------------------ Arrays ------------------------")
    print("#----------- Lista [] list()---------------------")
    #Las listas se pueden modificar
    listao = list(["danna", "yolanda", "joel", "daniel"])
    print(listao) #Devuelve la lista completa
    print(len(listao)) #Cant de objetos en una lista, en este caso 4
    print(listao[1]) #Devuelve el valor alojado en la posición 1 (Yolanda)
    listao[3] = "Modificar" #Esto SI Es valido en el código
    3
    print("#--------------- Tupla() tuple() --------------------")
    #Las tuplas no se pueden modificar, se quedan tal y como estan para siempre
    Tupla = tuple(("Manzana", "banana", "fresas"))
    print(Tupla)

    print("#--------------- Diccionario{*Key* : *Value*,} Dict() --------------------")
    Diccionario = {
        "Nombre": "Juan",
        "Edad": "16",
        "Apellido": "Rivero"
    }
    print(Diccionario) #Devuelve todo lo alojado en el dict
    print(Diccionario.get("Nombre")) # .get devuelve el valor que esta en clave
    print(Diccionario.keys()) #Devuelve todas las claves del dict

    print("#--------------- Conjuntos{} -------------------")
    # parecidos a las tuplas, no se accede a los elementos por su índice y tampoco almacena datos duplicados
    conjunto =  {"Juan","Juandariver9", 16, "Tutankamon", "Juandariver9"}
    print(conjunto) # {16, 'Juandariver9', 'Tutankamon', 'Juan'} El elemento juandariver9 al estar repetido solo se pone una vez
    #print(conjunto[3]) --> No puede acceder al elemento de su índice

    #-----------DESCRIPCIÓN EN 5 PALABRAS------------
    print("-----------DESCRIPCIÓN EN 5 PALABRAS------------\n")
    print("Listas: Ordenadas , Modificables, Indexables, Versatiles, Dinamicas\n")
    print("Tuplas: Inmutables, Indexables, Eficientes, Iterables, Fijas\n")
    print("Diccionarios: Asociativos, KeyValue, Modificables, Versatiles\n")
    print("Conjuntos: NoDuplicados, Inindexables, desordenados,Modificables\n")
    
def ejercicio4():
    import math

    def Colision(bola1, bola2):
        x1, y1 ,r1 = bola1
        x2, y2,r2 = bola2

        distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
        print(distance_euclides)

        return distance_euclides <= r1 + r2

    bola1 = (2, 6 , 2)
    bola2 = (2, 2, 2)

    print(Colision(bola1, bola2))
    
def ejerciciobonus():
    import math

    def Colision(bola1, bola2):
        x1, y1, z1 ,r1 = bola1
        x2, y2, z2 ,r2 = bola2

        distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) + (z2 - z1)**2
        print(distance_euclides)

        return distance_euclides <= r1 + r2

    bola1 = (6.5, 2, 4 , 2)
    bola2 = (6.5, 2, 2, 2)

    print(Colision(bola1, bola2))
    
    
    

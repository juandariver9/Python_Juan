def main(User, edad):
    #-----------------------------------------
    #--- Ejercicio 1 ---
    #-----------------------------------------
    #Impresión en consola
    print("Hello World"); # Imprime hola mundo en la consola
    # ------- Datos primitivos ------- 
    # 1. String
    texto = "Campus"
    print(type(texto))
    print(texto)
    # 2. Int
    NumEntero = 1
    print(type(NumEntero))
    print(NumEntero)
    # 3. Float
    NumDecimal = 3.1
    print(type(NumDecimal))
    print(NumDecimal)
    # 4. Double
    NumDecLargo = 3.141675827372
    print(type(NumDecLargo))
    print(NumDecLargo)
    # 5. Boolean
    Booleano = True
    print(type(Booleano))
    print(Booleano)

    #---------- Entradas parte usuario -------------
    print("Tu nombre es", User)
    #---------- Entradas parte usuario con definición de dato primitivo -------------
    print("Tu edad es", edad)

    #Ciclos
    #Ciclo for
    for i in range (5,10,2): #For contador in range (desde,hasta,pasos):
        print(i)
    #Ciclos while
    booleanito = True
    while booleanito == True: #while condicion_a_cumplir:
        print("Sigo vivo")
        booleanito = False
    # ------------------- Condicionales -----------------
    texto1 = "Campuss"
    if texto1 == "Campuss":
        print("Si es")
    else:
        print("no es")

def arrays():
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

def Funciones():
    print("#--------------------- Funciones def <nombre>(): ----------------")
    print("#Sin parametros y sin retorno")
    def SinSin():
        print("Hola Mundo!")
    SinSin()
    print("#Sin parametros y con retorno")
    def SinCon():
        c = 3 + 5
        return c
    print(SinCon())
    print("#Con Parametors y sin retorno")
    def ConSin(a, b):
        c = a + b
        print("La suma es: ", c)
    ConSin(10,20)
    print("#Con Parametros y Con retorno")
    def ConCon(x,y):
        n = x / y
        return round(n,2) #round es pa redondear dahh, y el 2 es para cuantos decimales se dejan
    x = float(input("Digite un número: "))
    y = float(input("Digite otro número: "))

    print (ConCon(x,y))
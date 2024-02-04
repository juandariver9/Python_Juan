import comandos1
while True:
    print("--------------")
    print("Que tarea desea ver, 0 si desea salir")
    print("1. main")
    print("2. Arrays")
    print("3. Funciones")
    des=int(input("--> "))
    print("--------------")

    if des == 1:
        User = str(input("Ingresa tu nombre -> "))
        edad = int(input("Ingresa tu edad -> "))
        print(comandos1.main(User, edad))
    elif des == 2:
        print(comandos1.arrays())
    elif des == 3:
        print(comandos1.Funciones())
    elif des == 0:
        print("Hasta luego!")
        break
    else:
        print("Tarea no identificada")
import comandos6
while True:
    print("Que ejercicio desea ver (Ingrese 0 si desea salir)")
    print("Ejercicio #1")
    print("Ejercicio #2")
    print("Ejercicio #3")
    print("Ejercicio #4")
    print("Ejercicio bonus")
    des=int(input("--> "))

    if des == 1:
        print("Ejercicio #1...")
        print(comandos6.ejercicio1())
    elif des == 2:
        print("Ejercicio #2...")
        print(comandos6.ejercicio2())
    elif des == 3:
        print("Ejercicio #3...")
        print(comandos6.ejercicio3())
    elif des == 4:
        print("Ejercicio #4...")
        print(comandos6.ejercicio4())
    elif des == 5:
        print("Ejercicio bonus...")
        print(comandos6.ejerciciobonus())
    elif des == 0:
        print("Hasta luego!")
        break
    else:
        print("Tarea no identificada")
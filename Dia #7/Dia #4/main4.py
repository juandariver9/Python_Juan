import comandos4
while True:
    print("Que juego desea ver (Ingrese 0 si desea salir)")
    print("1. Parejas")
    des=int(input("--> "))

    if des == 1:
        print("Así que escogiste Parejas... bien te explico:")
        print("Tendras que poner el número de casos que quieres, \nluego la lista de numeros de cada caso y k(la cual se diviran los pares entre este para saber si cumplen o no)")
        print(comandos4.Monedeas ())
    elif des == 0:
        print("Hasta luego!")
        break
    else:
        print("Tarea no identificada")
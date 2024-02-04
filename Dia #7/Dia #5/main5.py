import comandos5
while True:
    print("Que juego desea ver (Ingrese 0 si desea salir)")
    print("1. Mesas con monedas")
    des=int(input("--> "))

    if des == 1:
        print("Así que escogiste las mesas... bien te explico:")
        print("Tendras que poner el número de casos que quieres, \nLuego debes poner cuantos tipos de monedas y su altura")
        print(comandos5.mesas())
    elif des == 0:
        print("Hasta luego!")
        break
    else:
        print("Tarea no identificada")
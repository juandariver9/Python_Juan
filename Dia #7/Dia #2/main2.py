import comandos2
while True:
    print("--------------")
    print("Que juego desea ver (Ingrese 0 si desea salir)")
    print("1. Fibonacci")
    print("2. Juego interactivo")
    des=int(input("--> "))
    print("--------------")

    if des == 1:
        print("Así que escogiste Fibonacci... bien te explico:")
        print("La Secuencia de Fibonacci es una serie matemática en la que cada número es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). \nCaracterísticas notables incluyen su crecimiento exponencial, la convergencia hacia la proporción áurea /≈1.618/, \ny su presencia en patrones naturales y artísticos.\n")
        print(comandos2.Fibonacci ())
    elif des == 2:
        print("Así que escogiste el juego interactivo... Bien, te explico ")
        print("El juego va a generar un numero aleatorio entre 1 y 100 y tu tienes que adivinarlo.\nCada que escribas un número se te dirá si es menor o mayor \nTendras 10 intentos maximo para encontrar el resultado. ¡Suerte!\n")
        print(comandos2.Juegoi())
    elif des == 0:
        print("Hasta luego!")
        break
    else:
        print("Tarea no identificada")
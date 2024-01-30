import random

print("Bienvenido al juego de adivinanza\nIntenta adivinar el número secreto entre 1 y 100")

numero_secreto = random.randint(1, 100)
intentos_totales = 10

for intento_actual in range(1, intentos_totales + 1):
    try:
        Hipotesis = int(input(f"\nIntento {intento_actual}/{intentos_totales}. Ingresa tu Hipotesis: ")) #Solo me sirve con f strings
        #Hipotesis = int(input("Intento ",intento_actual," / ", intentos_totales, ". Ingresa tu hipotesis:")) <- no me dejo
        #Hipotesis = int(input("Intento " + intento_actual + " / "+ intentos_totales + ". Ingresa tu hipotesis:")) <- tampoco

        if Hipotesis < 1 or Hipotesis > 100:
            print("Ingrese un número entre 1 y 100")
            continue

        if Hipotesis == numero_secreto:
            print(f"\n¡Felicidades! adivinaste el número secreto ({numero_secreto}) en {intento_actual} intentos :DD")
            break
        elif Hipotesis < numero_secreto:
            print("El número secreto es mayor intenta de nuevo")
        else:
            print("El número secreto es menor intenta de nuevo")

    except:
        print("Ingrese un número valido")     
else:
    print(f"\nJa! Perdiste :( El número secreto era {numero_secreto}")
#Desarrollado por Juan David Rivero Romero 1096701639
# :DDDD
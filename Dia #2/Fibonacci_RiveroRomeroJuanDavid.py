def Secuencia(n):
    Fib = [0, 1]
    for i in range(2, n):
        Fib.append(Fib[i - 1] + Fib[i - 2])
    return Fib


print("Bienvenido al generador de la Secuencia de Fibonacci")

while True:
    try:
        n = int(input("\nIngrese el valor de 'n' para generar la secuencia (o ingrese 0 para salir): "))
        if n < 0:
            print("Por favor, ingrese un valor no negativo.")
            continue
        elif n == 0:
            print("Finalizaste el generador de Fibonacci.")
            break
        Fib = Secuencia(n)
        print("\nLa Secuencia de Fibonacci hasta el término ",n," es: ",Fib)
    except:
        print("Ingrese un valor entero valido")
#-----------------------------------------------------------------
#Desarrollado por Juan David Rivero Romero 1096701639
# :DDDD
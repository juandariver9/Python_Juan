def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1,1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

def main():
    print("¡Bienvenido al generador de la Secuencia de Fibonacci!")

    while True:
        try:
            n = int(input("\nIngrese el valor de 'n' para generar la secuencia (o ingrese 0 para salir): "))
            if n < 0:
                print("Por favor, ingrese un valor no negativo.")
                continue
            elif n == 0:
                print("¡Hasta luego! Gracias por usar el generador de Fibonacci.")
                break

            fib_sequence = fibonacci_sequence(n)
            print(f"\nLa Secuencia de Fibonacci hasta el término {n} es: {fib_sequence}")

        except ValueError:
            print("Por favor, ingrese un valor entero válido.")
#-----------------------------------------------------------------

main()

def Secuencia_Fibonacci(n):
    Fib = [0, 1]
    for i in range(2, n):
        Fib.append(Fib[i - 1] + Fib[i - 2])
    return Fib
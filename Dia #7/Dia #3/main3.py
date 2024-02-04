import comandos3

t = 1
while t > 0 or t < 1001:
    x = int(input("Ingrese un número: ")) #Entrada de número
    t = x
    if x < 1 or x > 1000:
        print("El código solo ejecuta números del 1 al 1000, Adios!")
        break # pa fuera
    else:
        print(comandos3.num_descompose(x)) #Llama la variable
#def numeros(x):
#    a = [10] * (x // 10)
#    b = [5] * ((x % 10) // 5)
#    c = [1] * ((x % 10) % 5)
#    return a + b + c
    
#x = int(input("digite un número "))

#print(numeros(x))

def num_descompose(x):
    return [10]* (x // 10) + [5] * ((x % 10) // 5) + [1] * ((x % 10) % 5)
t = 1
while t > 0 or t < 1001:
    numero = int(input("")) #Entrada de número
    t = numero
    if numero < 1 or numero > 1000:
        print("El código solo ejecuta números del 1 al 1000, Adios!")
        break # pa fuera
    else:
        print(num_descompose(numero)) #Llama la variable



#-------------------------------------------------------------
#Desarrollado por Juan David Rivero Romero 1096701639
# :DDDD
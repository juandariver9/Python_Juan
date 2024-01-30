def num_descompose(x):
    return [10]* (x // 10) + [5] * ((x % 10) // 5) + [1] * ((x % 10) % 5)

numero = int(input(""))
print(num_descompose(numero))

#-------------------------------------------------------------
#Desarrollado por Juan David Rivero Romero 1096701639
# :DDDD

#def numeros(x):
#    a = [10] * (x // 10)
#    b = [5] * ((x % 10) // 5)
#    c = [1] * ((x % 10) % 5)
#    return a + b + c
    
#x = int(input("digite un número "))

#print(numeros(x))

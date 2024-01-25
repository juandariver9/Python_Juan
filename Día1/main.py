#-----------------------------------------
#--- Ejercicio 1 ---
#-----------------------------------------

#Impresión en consola
print("Hello World"); # Imprime hola mundo en la consola

# ------- Datos primitivos ------- 
# 1. String
texto = "Campus"
print(type(texto))
print(texto)
# 2. Int
NumEntero = 1
print(type(NumEntero))
print(NumEntero)
# 3. Float
NumDecimal = 3.1
print(type(NumDecimal))
print(NumDecimal)
# 4. Double
NumDecLargo = 3.141675827372
print(type(NumDecLargo))
print(NumDecLargo)
# 5. Boolean
Booleano = True
print(type(Booleano))
print(Booleano)

#---------- Entradas parte usuario -------------
User = str(input("Digite su nombre: "))
print("Tu nombre es", User)
#---------- Entradas parte usuario con definición de dato primitivo -------------
User = int(input("Digite su edad: "))
print("Tu nombre es", User)


#Ciclos
#Ciclo for
for i in range (5,10,2): #For contador in range (desde,hasta,pasos):
    print(i)
#Ciclos while
booleanito = True
while booleanito == True: #while condicion_a_cumplir:
    print("Sigo vivo")
    booleanito = False
# ------------------- Condicionales -----------------
texto1 = "Campuss"
if texto1 == "Campuss":
    print("Si es")
else:
    print("no es")


#Desarrollado por Juan David Rivero Romero 1096701639
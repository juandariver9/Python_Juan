
Diccionario = {
    "Nombre": "Juan",
    "Apellido": "Rivero",
    "Edad": 16
}

print(Diccionario["Nombre"])
for i in Diccionario:
    print(i)
print("------------------------")
# Se pueden meter listas adentro del valor de los diccionarios
Diccionario = {
    "Nombre": ("Juan", "Andres", "Ruben", "Joel", "Daniel"),
    "Apellido": ("Rivero", "Santiago", "Ortiz", "Leon" , "Latorre"),
    "Edad": 16
}

print(Diccionario["Nombre"][2])
print(Diccionario)
print("------------------------")

#Recorrer un diccionario por valor

for i in Diccionario:
    print(i)

#Recorres un diccionario por las llaves
for valor in Diccionario:
    print(Diccionario[valor])
    
#Imprimir las llaves y valores de un diccionario
for llave , valor in Diccionario.items():
    print(llave,valor)

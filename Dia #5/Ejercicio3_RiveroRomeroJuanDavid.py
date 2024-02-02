#------------------ Arrays ------------------------
    #----------- Lista [] list()---------------------
    #Las listas se pueden modificar
listao = list(["danna", "yolanda", "joel", "daniel"])
print(listao) #Devuelve la lista completa
print(len(listao)) #Cant de objetos en una lista, en este caso 4
print(listao[1]) #Devuelve el valor alojado en la posición 1 (Yolanda)
listao[3] = "Modificar" #Esto SI Es valido en el código
3
#--------------- Tupla() tuple() --------------------
#Las tuplas no se pueden modificar, se quedan tal y como estan para siempre
Tupla = tuple(("Manzana", "banana", "fresas"))
print(Tupla)

#--------------- Diccionario{"Key" : "Value",} Dict() --------------------
Diccionario = {
    "Nombre": "Juan",
    "Edad": "16",
    "Apellido": "Rivero"
}
print(Diccionario) #Devuelve todo lo alojado en el dict
print(Diccionario.get("Nombre")) # .get devuelve el valor que esta en clave
print(Diccionario.keys()) #Devuelve todas las claves del dict

#--------------- Conjuntos{} -------------------
#parecidos a las tuplas, no se accede a los elementos por su índice y tampoco almacena datos duplicados
conjunto =  {"Juan","Juandariver9", 16, "Tutankamon", "Juandariver9"}
print(conjunto) # {16, 'Juandariver9', 'Tutankamon', 'Juan'} El elemento juandariver9 al estar repetido solo se pone una vez
#print(conjunto[3]) --> No puede acceder al elemento de su índice

#-----------DESCRIPCIÓN EN 5 PALABRAS------------
print("-----------DESCRIPCIÓN EN 5 PALABRAS------------\n")
print("Listas: Ordenadas , Modificables, Indexables, Versatiles, Dinamicas\n")
print("Tuplas: Inmutables, Indexables, Eficientes, Iterables, Fijas\n")
print("Diccionarios: Asociativos, KeyValue, Modificables, Versatiles\n")
print("Conjuntos: NoDuplicados, Inindexables, desordenados,Modificables\n")
import json

crudbase = open("aea.json")
crud = json.load(crudbase)

#CRUD clientes
clientes = crud["ventas"]["clientes"]

#CRUD comerciales
comerciales = crud["ventas"]["comerciales"]

#CRUD pedidos
pedidos = crud["ventas"]["pedidos"]

print("Ingrese que desea ver de la carpeta VENTAS")
print("")
print("Clientes, comerciales o pedidos.")
print("")
respuesta = str(input())
respuestafinal=respuesta.lower()
if respuestafinal == "clientes":
    print("")
    for i in clientes:
        print(i)
elif respuestafinal == "comerciales":
    print("")
    for j in comerciales:
        print(j)
elif respuestafinal == "pedidos":
    print("")
    for d in pedidos:
        print(d)
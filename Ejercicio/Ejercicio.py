import json
import ClientesCRUD
import ComercialesCRUD
import PedidosCRUD

crudbase = open("aea.json")
crud = json.load(crudbase)

#CRUD clientes
clientes = crud["ventas"]["clientes"]

#CRUD comerciales
comerciales = crud["ventas"]["comerciales"]

#CRUD pedidos
pedidos = crud["ventas"]["pedidos"]
while True:
    print("Ingrese que desea ver de la carpeta VENTAS")
    print("")
    print("Clientes, comerciales o pedidos.")
    print("")
    respuesta = str(input())
    respuestafinal=respuesta.lower()
    while True:
        if respuestafinal == "clientes":
            print("")
            for i in clientes:
                print(i)
            print("\nQue desea hacer con estos datos?")
            print("1.\t\t Añadir")
            print("2.\t\t Actualizar")
            print("3.\t\t Eliminar")
            print("Otro numero.\t Salir")
            CrudRespuesta = int(input(""))
            if CrudRespuesta == 1:
                print(ClientesCRUD.mainClientesAñadir())
            elif CrudRespuesta == 2:
                print(ClientesCRUD.MainClientesActualizar())
            elif CrudRespuesta == 3:
                print(ClientesCRUD.MainClientesEliminar())
            else:
                break
        
        elif respuestafinal == "comerciales":
            print("")
            for j in comerciales:
                print(j)
            print("\nQue desea hacer con estos datos?")
            print("1.\t\t Añadir")
            print("2.\t\t Actualizar")
            print("3.\t\t Eliminar")
            print("Otro numero.\t Salir")
            CrudRespuesta = int(input("--------->"))
            if CrudRespuesta == 1:
                print(ComercialesCRUD.mainComercialesAñadir())
            elif CrudRespuesta == 2:
                print(ComercialesCRUD.MainComercialesActualizar())
            elif CrudRespuesta == 3:
                print(ComercialesCRUD.MainComercialesEliminar())
            else:
                break
        elif respuestafinal == "pedidos":
            print("")
            for d in pedidos:
                print(d)
            print("\nQue desea hacer con estos datos?")
            print("1.\t\t Añadir")
            print("2.\t\t Actualizar")
            print("3.\t\t Eliminar")
            print("Otro numero.\t Salir")
            CrudRespuesta = int(input("--------->"))
            if CrudRespuesta == 1:
                print(PedidosCRUD.mainPedidosAñadir())
            elif CrudRespuesta == 2:
                print(PedidosCRUD.MainPedidosActualizar())
            elif CrudRespuesta == 3:
                print(PedidosCRUD.MainPedidosEliminar())
            else:
                break
        else:
            print("Bye!")
            break
    if respuestafinal != "clientes" or respuestafinal != "comerciales" or respuestafinal != "pedidos":
        print("Hasta luego!")
        break
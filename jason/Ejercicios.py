import json
#-----------------------Ejercicio 1-----------------------
with open("aea.json",'r') as ArchivoJson:
    ejercicio = json.load(ArchivoJson)
def ObtenerFecha(pedido):
    return pedido["fecha"]

pedidos = ejercicio["ventas"]["pedidos"]

PedidosOrdenados = sorted(pedidos, key=ObtenerFecha, reverse=True)

#print(pedidos_ordenados)

with open('Ejercicio1.json', 'w') as outfile:
    json.dump(PedidosOrdenados, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 2-----------------------
with open("aea.json",'r') as file:
    ejercicio = json.load(file)
    
def ObtenerTotal(pedido):
    return pedido["total"]

pedidos = ejercicio["ventas"]["pedidos"]

PedidosOrdenados = sorted(pedidos, key=ObtenerTotal, reverse=True)[:2]

#print(pedidos_ordenados)

with open('Ejercicio2.json', 'w') as outfile:
    json.dump(PedidosOrdenados, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 3-----------------------

with open('aea.json', 'r') as file:
    ejercicio = json.load(file)
    
ClientesConPedidos = set() #<- almacenarlos en un conjunto para que no sw repitan
for pedido in ejercicio["ventas"]["pedidos"]:
    ClientesConPedidos.add(pedido["id_cliente"]) # <- se añaden los pedidos
# print(clientes_con_pedidos)

ClientesConPedidos = list(ClientesConPedidos) # <- el conjunto lo pasamos a lista

with open('Ejercicio3.json', 'w') as outfile:
    json.dump(ClientesConPedidos, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 4-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

Pedidos2017Mas500 = []

for pedido in ejercicio["ventas"]["pedidos"]:
    
    año_pedido = int(pedido["fecha"].split("-")[0]) #dividir el valor de fecha de acuerdo a los - y solo agarrar el primero (Año)
    
    if año_pedido == 2017 and pedido["total"] > 500:
        Pedidos2017Mas500.append(pedido)

with open('Ejercicio4.json', 'w') as outfile:
    json.dump(Pedidos2017Mas500, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 5-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

ComercialesQueCumplen = []

for comercial in ejercicio["ventas"]["comerciales"]:
    
    comision = comercial["comision"]

    if 0.05 <= comision <= 0.11:
        nombre_apellidos = f"{comercial['nombre']} {comercial['apellido1']} {comercial['apellido2']}"
        ComercialesQueCumplen.append(nombre_apellidos)

with open('Ejercicio5.json', 'w') as outfile:
    json.dump(ComercialesQueCumplen, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 6-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

MayorComision = 0

for comercial in ejercicio["ventas"]["comerciales"]:
    
    comision = comercial["comision"]
    
    if comision > MayorComision:
        MayorComision = comision

with open('Ejercicio6.json', 'w') as outfile:
    json.dump({"MayorComision": MayorComision}, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 7-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

ListaSevilleros = []
for clients in ejercicio["ventas"]["clientes"]:
    ciudad = clients["ciudad"]
    
    if ciudad == "Sevilla":
        IdNombreApellido = f"Id:{clients['id']} Nombre: {clients['apellido1']} {clients['nombre']}"
        ListaSevilleros.append(IdNombreApellido)
        ListaSevilleros = sorted(ListaSevilleros)

with open('Ejercicio7.json', 'w') as outfile:
    json.dump(ListaSevilleros, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 8-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

ListaPersonas = []

for clients in ejercicio["ventas"]["clientes"]:
    NombresClientes = str(clients["nombre"])
    EmpiezanA = NombresClientes.startswith("A")
    EmpiezanP = NombresClientes.startswith("P")
    TerminanN = NombresClientes.endswith("n")
    if EmpiezanA == True and TerminanN == True:
        NombreC =  f"{clients['nombre']}"
        ListaPersonas.append(NombreC)
    elif EmpiezanP == True:
        NombreC =  f"{clients['nombre']}"
        ListaPersonas.append(NombreC)
        ListaPersonas = sorted(ListaPersonas)

with open('Ejercicio8.json', 'w') as outfile:
    json.dump(ListaPersonas, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 9-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

ListaPersonas = []

for clients in ejercicio["ventas"]["clientes"]:
    NombresClientes = str(clients["nombre"])
    EmpiezanA = NombresClientes.startswith("A")
    if EmpiezanA == True:
        NombreC =  f"{clients['nombre']} "
        ListaPersonas.append(NombreC)
        ListaPersonas = sorted(ListaPersonas)

with open('Ejercicio9.json', 'w') as outfile:
    json.dump(ListaPersonas, outfile, indent=2)
#---------------------------------------------------------
#-----------------------Ejercicio 10-----------------------
with open('aea.json', 'r') as file:
    ejercicio = json.load(file)

ListaRuiz = []

for Comercials in ejercicio["ventas"]["comerciales"]:
    NombresClientes = str(Comercials["apellido1"])
    Ruiz = NombresClientes.startswith("Ruiz")
    if Ruiz == True:
        NombreC =  f"{Comercials['nombre']} {Comercials['apellido1']} "
        ListaRuiz.append(NombreC)
        ListaRuiz = sorted(ListaRuiz)

with open('Ejercicio10.json', 'w') as outfile:
    json.dump(ListaRuiz, outfile, indent=2)
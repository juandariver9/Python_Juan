import json

with open("aea.json",'r') as archivo_json:
    ejercicio = json.load(archivo_json)
#-----------------------Ejercicio 1-----------------------
def obtener_fecha(pedido):
    return pedido["fecha"]

pedidos = ejercicio["ventas"]["pedidos"]

pedidos_ordenados = sorted(pedidos, key=obtener_fecha, reverse=True)

#print(pedidos_ordenados)

# Escribir los pedidos ordenados en un nuevo archivo JSON
with open('Ejercicio1.json', 'w') as outfile:
    json.dump(pedidos_ordenados, outfile, indent=2)
#---------------------------------------------------------
def obtener_fecha(pedido):
    return pedido["total"]

pedidos = ejercicio["ventas"]["pedidos"]

pedidos_ordenados = sorted(pedidos, key=obtener_fecha, reverse=True)[:2]

#print(pedidos_ordenados)

# Escribir los primeros dos pedidos ordenados en un nuevo archivo JSON
with open('Ejercicio2.json', 'w') as outfile:
    json.dump(pedidos_ordenados, outfile, indent=2)
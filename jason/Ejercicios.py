import json
entrada = 'aea.json'
with open(entrada,'r') as archivo:
    datos = json.load(archivo)

for llave , valor in datos.items():
    for llave, valor in datos['ventas'].items():
        print(llave,valor)
print(type(datos))
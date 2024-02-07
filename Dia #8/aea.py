import json

# Ejemplo de datos en formato JSON
datos_json = '''
{
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Ciudad de Mexico",
  "intereses": ["programacion", "fotografia", "viajes"]
}
'''

# Parsear el JSON a un diccionario de Python
datos = json.loads(datos_json)

# Acceder a los datos
print("Nombre:", datos["nombre"])
print("Edad:", datos["edad"])
print("Ciudad:", datos["ciudad"])
print("Intereses:", ", ".join(datos["intereses"]))

# Modificar los datos
datos["edad"] = 31
datos["intereses"].append("montanismo")

# Convertir el diccionario de Python de nuevo a JSON
nuevos_datos_json = json.dumps(datos, indent=2)

# Imprimir los nuevos datos en formato JSON
print("\nNuevos datos en formato JSON:")
print(nuevos_datos_json)

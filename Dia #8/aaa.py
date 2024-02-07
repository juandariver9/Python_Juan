import json

# Función para ingresar datos del usuario
def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su ciudad: ")
    intereses = input("Ingrese sus intereses separados por coma: ").split(", ")
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad, "intereses": intereses}

# Función para guardar datos en un archivo JSON
def guardar_datos(datos, archivo):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=2)
    print("Datos guardados exitosamente en", archivo)

# Función para cargar datos desde un archivo JSON
def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("El archivo especificado no existe. Creando uno nuevo.")
        return False

# Función principal
def main():
    archivo = "datos.json"

    # Intentar cargar datos existentes
    datos_guardados = cargar_datos(archivo)

    if datos_guardados:
        print("Datos cargados del archivo:")
        print(json.dumps(datos_guardados, indent=2))
        opcion = input("¿Desea modificar los datos? (si/no): ").lower()
        if opcion == "si":
            nuevos_datos = ingresar_datos()
            guardar_datos(nuevos_datos, archivo)
        else:
            print("Saliendo sin modificar los datos.")
    else:
        print("No se encontraron datos guardados.")
        nuevos_datos = ingresar_datos()
        guardar_datos(nuevos_datos, archivo)

if __name__ == "__main__":
    main()

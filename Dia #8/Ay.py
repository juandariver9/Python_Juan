import json

# Función para ingresar datos de una persona
def ingresar_datos_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    ciudad = input("Ingrese la ciudad de la persona: ")
    intereses = input("Ingrese los intereses de la persona separados por coma: ").split(", ")
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
        return []

# Función principal
def main():
    archivo = "datos_personas.json"

    # Intentar cargar datos existentes
    datos_guardados = cargar_datos(archivo)

    # Mostrar datos existentes
    if datos_guardados:
        print("Datos cargados del archivo:")
        for idx, persona in enumerate(datos_guardados, start=1):
            print(f"Persona {idx}:")
            print(json.dumps(persona, indent=2))
    
    # Pedir datos de una nueva persona
    nueva_persona = ingresar_datos_persona()
    datos_guardados.append(nueva_persona)
    guardar_datos(datos_guardados, archivo)

if __name__ == "__main__":
    main()

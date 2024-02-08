import json

def cargar_datos_json():
    try:
        with open("ventasClientes.json", 'r') as infile:
            datos = json.load(infile)
            return datos
    except FileNotFoundError:
        return []

def guardar_datos_json(datos):
    with open("ventasClientes.json", 'w') as outfile:
        json.dump(datos, outfile, indent=2)

def ingresar_datos_persona():
    datos_personas = cargar_datos_json()

    contador = len(datos_personas) + 1 
    
    while True:
        Apellidos = int(input("La persona tiene más de uno o dos apellidos (1/2), o 0 para terminar: "))
        if Apellidos == 0:
            break
        elif Apellidos == 1:
            nombre = input("Ingrese el nombre de la persona: ")
            apellido1 = input("Ingrese el apellido de la persona: ")
            ciudad = input("Ingrese la ciudad de la persona: ")
            categoria = input("Ingrese la categoría de la persona: ")
            datos_personas.append({"Id": contador, "nombre": nombre, "apellido1": apellido1, "ciudad": ciudad, "categoría": categoria})
        elif Apellidos == 2:
            nombre = input("Ingrese el nombre de la persona: ")
            apellido1 = input("Ingrese el primer apellido de la persona: ")
            apellido2 = input("Ingrese el segundo apellido de la persona: ")
            ciudad = input("Ingrese la ciudad de la persona: ")
            categoria = input("Ingrese la categoría de la persona: ")
            datos_personas.append({"Id": contador, "nombre": nombre, "apellido1": apellido1,"apellido2": apellido2 ,"ciudad": ciudad, "categoría": categoria})
        
        contador += 1

        print("\nDatos ingresados hasta el momento:")
        for persona in datos_personas:
            print(persona)
        
        continuar = input("\n¿Desea seguir añadiendo datos? (s/n): ").lower()
        if continuar != 's':
            break
    
    guardar_datos_json(datos_personas)

ingresar_datos_persona()


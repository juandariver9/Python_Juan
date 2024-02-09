def mainComercialesAñadir():
    import json

    def cargar_datos_json():
        try:
            with open("aea.json", 'r') as infile:
                datos = json.load(infile)
                return datos
        except FileNotFoundError:
            return {"ventas": {"clientes": [], "comerciales": [], "pedidos": []}}

    def obtener_proximo_id(datos, tipo_entidad):
        if datos and tipo_entidad in datos["ventas"]:
            ids = [item["id"] for item in datos["ventas"][tipo_entidad]]
            return max(ids) + 1
        else:
            return 1

    def guardar_datos_json(datos):
        with open("aea.json", 'w') as outfile:
            json.dump(datos, outfile, indent=2)

    def reindexar_ids(datos):
        comerciales = datos["ventas"]["comerciales"]
        for i, cliente in enumerate(comerciales, 1):
            cliente["id"] = i

    def ingresar_datos_comerciales():
        datos_json = cargar_datos_json()
        contador = obtener_proximo_id(datos_json, "comerciales")
        nombre = input("Ingrese el nombre del comercial: ")
        apellido1 = input("Ingrese el primer apellido del comercial: ")
        apellido2 = input("Ingrese el segundo apellido del comercial (opcional): ")
        comision = float(input("Ingrese la comision del comercial: "))
        if apellido2:
            nuevo_cliente = { 
                "id": contador,
                "nombre": nombre,
                "apellido1": apellido1,
                "apellido2": apellido2,
                "comision": comision
                } 
        else:
            nuevo_cliente = {
                "id": contador,
                "nombre": nombre,
                "apellido1": apellido1,
                "comision": comision
                }
        datos_json["ventas"]["comerciales"].append(nuevo_cliente)
        guardar_datos_json(datos_json)
        print("Comercial agregado correctamente.")

    # Puedes agregar funciones similares para ingresar datos de comerciales y pedidos si lo deseas.

    ingresar_datos_comerciales()

    # Reindexar los IDs al finalizar el programa
    datos_json = cargar_datos_json()
    reindexar_ids(datos_json)
    guardar_datos_json(datos_json)
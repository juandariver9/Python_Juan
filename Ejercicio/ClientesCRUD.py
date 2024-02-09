def mainClientesAñadir():
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
        clientes = datos["ventas"]["clientes"]
        for i, cliente in enumerate(clientes, 1):
            cliente["id"] = i

    def ingresar_datos_cliente():
        datos_json = cargar_datos_json()
        contador = obtener_proximo_id(datos_json, "clientes")
        nombre = input("Ingrese el nombre del cliente: ")
        apellido1 = input("Ingrese el primer apellido del cliente: ")
        apellido2 = input("Ingrese el segundo apellido del cliente (opcional): ")
        ciudad = input("Ingrese la ciudad del cliente: ")
        categoria = input("Ingrese la categoría del cliente: ")
        if apellido2:
            nuevo_cliente = { 
                "id": contador,
                "nombre": nombre,
                "apellido1": apellido1,
                "apellido2": apellido2,
                "ciudad": ciudad,
                "categoría": categoria
                } 
        else:
            nuevo_cliente = {
                "id": contador,
                "nombre": nombre,
                "apellido1": apellido1,
                "ciudad": ciudad,
                "categoría": categoria
                }
        datos_json["ventas"]["clientes"].append(nuevo_cliente)
        guardar_datos_json(datos_json)
        print("Cliente agregado correctamente.")

    # Puedes agregar funciones similares para ingresar datos de comerciales y pedidos si lo deseas.

    ingresar_datos_cliente()

    # Reindexar los IDs al finalizar el programa
    datos_json = cargar_datos_json()
    reindexar_ids(datos_json)
    guardar_datos_json(datos_json)
def MainClientesEliminar():
    import json

    def cargar_datos_json():
        try:
            with open("aea.json", 'r') as infile:
                datos = json.load(infile)
                return datos
        except FileNotFoundError:
            return {"ventas": {"clientes": [], "comerciales": [], "pedidos": []}}

    def guardar_datos_json(datos):
        with open("aea.json", 'w') as outfile:
            json.dump(datos, outfile, indent=2)

    def reindexar_ids(datos):
        clientes = datos["ventas"]["clientes"]
        for i, cliente in enumerate(clientes, 1):
            cliente["id"] = i

    def eliminar_cliente(datos, id_cliente):
        clientes = datos["ventas"]["clientes"]
        cliente_eliminado = None
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                cliente_eliminado = cliente
                clientes.remove(cliente)
                break
        return cliente_eliminado

    def eliminar_datos_cliente():
        datos_json = cargar_datos_json()
        id_cliente = int(input("Ingrese el ID del cliente que desea eliminar: "))
        cliente_eliminado = eliminar_cliente(datos_json, id_cliente)
        if cliente_eliminado:
            guardar_datos_json(datos_json)
            print("Cliente eliminado correctamente:")
            print(cliente_eliminado)
            reindexar_ids(datos_json)
            guardar_datos_json(datos_json)
        else:
            print("No se encontró ningún cliente con el ID proporcionado.")
    eliminar_datos_cliente()

def MainClientesActualizar():
    import json

    def cargar_datos_json():
        try:
            with open("aea.json", 'r') as infile:
                datos = json.load(infile)
                return datos
        except FileNotFoundError:
            return {"ventas": {"clientes": [], "comerciales": [], "pedidos": []}}

    def guardar_datos_json(datos):
        with open("aea.json", 'w') as outfile:
            json.dump(datos, outfile, indent=2)

    def actualizar_cliente(datos, id_cliente, nuevo_cliente):
        clientes = datos["ventas"]["clientes"]
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                cliente.update(nuevo_cliente)
                return cliente
        return None

    def actualizar_datos_cliente():
        datos_json = cargar_datos_json()
        id_cliente = int(input("Ingrese el ID del cliente que desea actualizar: "))
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        apellido1 = input("Ingrese el nuevo primer apellido del cliente: ")
        apellido2 = input("Ingrese el nuevo segundo apellido del cliente (opcional): ")
        ciudad = input("Ingrese la nueva ciudad del cliente: ")
        categoria = input("Ingrese la nueva categoría del cliente: ")
        if apellido2:
            nuevo_cliente = {
                "nombre": nombre,
                "apellido1": apellido1,
                "apellido2": apellido2,
                "ciudad": ciudad,
                "categoría": categoria
            }
        else:
            nuevo_cliente = {
                "nombre": nombre,
                "apellido1": apellido1,
                "ciudad": ciudad,
                "categoría": categoria
            }   
            

        cliente_actualizado = actualizar_cliente(datos_json, id_cliente, nuevo_cliente)
        if cliente_actualizado:
            guardar_datos_json(datos_json)
            print("Cliente actualizado correctamente:")
            print(cliente_actualizado)
        else:
            print("No se encontró ningún cliente con el ID proporcionado.")

    actualizar_datos_cliente()
import os
from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar la lista de productos.
    Ahora incluye persistencia en archivos y manejo de excepciones.
    """

    def __init__(self):
        # Lista en memoria
        self.productos = []

        # ----------- RUTAS DINÁMICAS -----------
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.registros_dir = os.path.join(self.base_dir, "registros")
        self.archivo_inventario = os.path.join(self.registros_dir, "inventario.txt")

        # Crear carpeta registros si no existe
        os.makedirs(self.registros_dir, exist_ok=True)

        # Cargar productos existentes
        self.cargar_desde_archivo()

    # ======================================================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ======================================================
    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo_inventario):
                # Crear archivo si no existe
                with open(self.archivo_inventario, "w") as f:
                    pass
                return

            with open(self.archivo_inventario, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")

                    if len(datos) == 4:
                        id_producto = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)

        except FileNotFoundError:
            print("Archivo de inventario no encontrado.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    # ======================================================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ======================================================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo_inventario, "w") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)
            return True

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")
            return False

    # ======================================================
    # MÉTODOS CRUD
    # ======================================================
    def añadir_producto(self, producto: Producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID repetido.")
                return False

        self.productos.append(producto)

        if self.guardar_en_archivo():
            print("Producto añadido y guardado en archivo correctamente.")
            return True
        return False

    def eliminar_producto(self, id_producto: int):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)

                if self.guardar_en_archivo():
                    print("Producto eliminado y archivo actualizado.")
                    return True
                return False

        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto: int, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                if self.guardar_en_archivo():
                    print("Producto actualizado y archivo guardado.")
                    return True
                return False

        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre: str):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for p in self.productos:
                print(p)

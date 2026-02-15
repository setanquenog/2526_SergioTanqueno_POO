# servicios/inventario.py

from modelos.producto import Producto

class Inventario:
    """
    Clase encargada de gestionar la lista de productos.
    Sus métodos son llamados desde main.py según la opción seleccionada.
    """

    def __init__(self):
        self.productos = []  # Lista principal de almacenamiento


    # ----------- AÑADIR -----------
    # Se utiliza cuando el usuario selecciona:
    # Opción 1 en el menú (Añadir producto)
    # Llamado desde main.py:
    # inventario.añadir_producto(producto)

    def añadir_producto(self, producto: Producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        print("Producto añadido correctamente.")
        return True


    # ----------- ELIMINAR -----------
    # Se utiliza cuando el usuario selecciona:
    # Opción 2 (Eliminar producto)
    # Llamado desde main.py:
    # inventario.eliminar_producto(id_producto)

    def eliminar_producto(self, id_producto: int):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return True

        print("Producto no encontrado.")
        return False


    # ----------- ACTUALIZAR -----------
    # Se utiliza cuando el usuario selecciona:
    # Opción 3 (Actualizar producto)
    # Llamado desde main.py:
    # inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

    def actualizar_producto(self, id_producto: int, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return True

        print("Producto no encontrado.")
        return False


    # ----------- BUSCAR -----------
    # Se utiliza cuando el usuario selecciona:
    # Opción 4 (Buscar producto)
    # Llamado desde main.py:
    # resultados = inventario.buscar_por_nombre(nombre)

    def buscar_por_nombre(self, nombre: str):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados


    # ----------- LISTAR -----------
    # Se utiliza cuando el usuario selecciona:
    # Opción 5 (Listar inventario)
    # Llamado desde main.py:
    # inventario.mostrar_inventario()

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for p in self.productos:
                print(p)



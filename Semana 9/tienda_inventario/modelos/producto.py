# modelos/producto.py

class Producto:
    """
    Clase que representa un producto dentro del inventario.
    Se utiliza cuando el usuario selecciona la opción 1 (Añadir producto)
    en el menú principal de main.py.
    """

    # ----------- CONSTRUCTOR ----------
    # Se utiliza en main.py cuando el usuario crea un nuevo producto:
    # producto = Producto(id_producto, nombre, cantidad, precio)
    # (Opción 1 del menú: Añadir producto)
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio


    # ----------- GETTERS -----------
    # Se utilizan en inventario.py para:
    # - Validar que el ID no esté repetido (añadir_producto)
    # - Buscar producto por ID (eliminar, actualizar)
    # - Buscar por nombre (buscar_por_nombre)
    # - Mostrar información del producto

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio


    # ----------- SETTERS -----------
    # Se utilizan en inventario.py dentro del método actualizar_producto()
    # cuando el usuario selecciona la opción 3 (Actualizar producto).
    # Permiten modificar cantidad o precio validando que no sean negativos.

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_cantidad(self, cantidad: int):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio: float):
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo.")


    # ----------- MÉTODO STR -----------
    # Se utiliza cuando:
    # - Se listan productos (opción 5: Listar inventario)
    # - Se muestran resultados de búsqueda (opción 4: Buscar producto)
    # Permite imprimir el objeto de forma legible.
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
# servicios/inventario_servicio.py

import os
from modelos.producto import Producto

# =========================
# RUTAS DEL SISTEMA
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_REGISTROS = os.path.join(BASE_DIR, "registros")

ARCHIVO_INVENTARIO = os.path.join(RUTA_REGISTROS, "inventario.txt")
ARCHIVO_MENU = os.path.join(RUTA_REGISTROS, "menu.txt")


class InventarioServicio:
    def __init__(self):
        os.makedirs(RUTA_REGISTROS, exist_ok=True)

        # =====================================================
        # DICCIONARIO (dict)
        # Colección principal del sistema
        # Clave   → id_producto (único)
        # Valor   → objeto Producto
        # =====================================================
        self.productos = {}   # dict[str, Producto]

    # =====================================================
    # REGISTRO DE ACCIONES (archivo de texto)
    # =====================================================
    def registrar_menu(self, mensaje):
        with open(ARCHIVO_MENU, "a", encoding="utf-8") as f:
            f.write(mensaje + "\n")

    # =====================================================
    # ARCHIVOS (LECTURA / ESCRITURA)
    # =====================================================
    def guardar_archivo(self):
        with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
            # Iteración sobre los valores del diccionario
            for producto in self.productos.values():
                f.write(str(producto) + "\n")

    def cargar_archivo(self):
        if not os.path.exists(ARCHIVO_INVENTARIO):
            open(ARCHIVO_INVENTARIO, "w", encoding="utf-8").close()
            return

        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    # =================================================
                    # TUPLA (tuple)
                    # El método split() devuelve una tupla
                    # Se usa desempaquetado de tupla
                    # =================================================
                    id_p, nombre, cantidad, precio = linea.strip().split(",")

                    self.productos[id_p] = Producto(
                        id_p, nombre, int(cantidad), float(precio)
                    )

    # =====================================================
    # CRUD
    # =====================================================
    def agregar_producto(self, producto):
        # =================================================
        # CONJUNTO (set) – uso conceptual
        # Las claves del diccionario funcionan como un set
        # Garantizan que los IDs sean únicos
        # =================================================
        if producto.get_id() in self.productos:
            print("⚠️ El producto ya existe.")
            self.registrar_menu(f"Error al agregar: {producto.get_id()}")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_archivo()
        self.registrar_menu(f"Producto agregado: {producto.get_id()}")
        print("✅ Producto agregado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_archivo()
            self.registrar_menu(f"Producto eliminado: {id_producto}")
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")
            self.registrar_menu(f"Error al eliminar: {id_producto}")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print("❌ Producto no existe.")
            self.registrar_menu(f"Error al actualizar: {id_producto}")
            return

        producto = self.productos[id_producto]
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

        self.guardar_archivo()
        self.registrar_menu(f"Producto actualizado: {id_producto}")
        print("✏️ Producto actualizado.")

    def buscar_por_nombre(self, nombre):
        # =================================================
        # LISTA (list)
        # Se usa una lista por comprensión para almacenar
        # resultados temporales de búsqueda
        # =================================================
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        self.registrar_menu(f"Búsqueda por nombre: {nombre}")

        if not encontrados:
            print("❌ No se encontraron productos.")
            return

        for p in encontrados:
            self.mostrar_producto(p)

    def mostrar_todos(self):
        if not self.productos:
            print("📭 Inventario vacío.")
            return

        self.registrar_menu("Listado de inventario")
        for p in self.productos.values():
            self.mostrar_producto(p)

    def mostrar_producto(self, producto):
        print(
            f"ID: {producto.get_id()} | "
            f"Nombre: {producto.get_nombre()} | "
            f"Cantidad: {producto.get_cantidad()} | "
            f"Precio: ${producto.get_precio():.2f}"
        )
# main.py

from modelos.producto import Producto
from servicios.inventario_servicio import InventarioServicio


def menu():
    inventario = InventarioServicio()
    inventario.cargar_archivo()
    inventario.registrar_menu("=== SISTEMA INICIADO ===")

    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1) Agregar producto")
        print("2) Eliminar producto")
        print("3) Actualizar producto")
        print("4) Buscar por nombre")
        print("5) Mostrar inventario")
        print("0) Salir")

        opcion = input("Opción: ").strip()
        inventario.registrar_menu(f"Opción seleccionada: {opcion}")

        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(
                Producto(id_p, nombre, cantidad, precio)
            )

        elif opcion == "2":
            inventario.eliminar_producto(input("ID a eliminar: "))

        elif opcion == "3":
            id_p = input("ID: ")
            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")

            inventario.actualizar_producto(
                id_p,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            inventario.buscar_por_nombre(input("Nombre a buscar: "))

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "0":
            inventario.guardar_archivo()
            inventario.registrar_menu("=== SISTEMA FINALIZADO ===")
            print("👋 Saliendo...")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    menu()
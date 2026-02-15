# main.py

from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            continue

        if opcion == 1:
            try:
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print("Error en los datos ingresados.")

        elif opcion == 2:
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("ID inválido.")

        elif opcion == 3:
            try:
                id_producto = int(input("ID del producto a actualizar: "))

                print("Deje en blanco si no desea modificar un campo.")

                cantidad_input = input("Nueva cantidad: ")
                precio_input = input("Nuevo precio: ")

                nueva_cantidad = int(cantidad_input) if cantidad_input else None
                nuevo_precio = float(precio_input) if precio_input else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Datos inválidos.")

        elif opcion == 4:
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == 5:
            inventario.mostrar_inventario()

        elif opcion == 6:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
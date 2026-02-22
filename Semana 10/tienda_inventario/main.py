import os
from modelos.producto import Producto
from servicios.inventario import Inventario


def crear_archivo_menu(base_dir):
    registros_dir = os.path.join(base_dir, "registros")
    os.makedirs(registros_dir, exist_ok=True)

    archivo_menu = os.path.join(registros_dir, "menu.txt")

    try:
        with open(archivo_menu, "w") as f:
            f.write("===== SISTEMA DE INVENTARIO =====\n")
            f.write("1. Añadir producto\n")
            f.write("2. Eliminar producto\n")
            f.write("3. Actualizar producto\n")
            f.write("4. Buscar producto\n")
            f.write("5. Listar inventario\n")
            f.write("6. Salir\n")
        print("Archivo menu.txt creado correctamente.")
    except PermissionError:
        print("No se pudo crear menu.txt por falta de permisos.")
    except Exception as e:
        print(f"Error al crear menu.txt: {e}")


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    crear_archivo_menu(base_dir)

    inventario = Inventario()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            try:
                producto = Producto(
                    int(input("ID: ")),
                    input("Nombre: "),
                    int(input("Cantidad: ")),
                    float(input("Precio: "))
                )
                inventario.añadir_producto(producto)
            except ValueError:
                print("Datos inválidos.")

        elif opcion == 2:
            inventario.eliminar_producto(int(input("ID a eliminar: ")))

        elif opcion == 3:
            id_producto = int(input("ID a actualizar: "))
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == 4:
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for p in resultados:
                print(p)

        elif opcion == 5:
            inventario.mostrar_inventario()

        elif opcion == 6:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
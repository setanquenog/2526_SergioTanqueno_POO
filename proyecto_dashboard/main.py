import os

from modelos.menu import Menu
from servicios.navegador_codigo import mostrar_scripts


def mostrar_sub_menu(ruta_unidad):
    subcarpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú:")
        for i, carpeta in enumerate(subcarpetas, start=1):
            print(f"{i} - {carpeta}")

        print("0 - Regresar")

        opcion = input("Seleccione una subcarpeta: ")

        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(subcarpetas):
                mostrar_scripts(os.path.join(ruta_unidad, subcarpetas[indice]))
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    menu = Menu()

    while True:
        print("\nDashboard - Menú Principal")
        for clave, valor in menu.obtener_unidades().items():
            print(f"{clave} - {valor}")

        print("0 - Salir")

        opcion = input("Seleccione una unidad: ")

        if opcion == '0':
            print("Saliendo del sistema.")
            break
        elif opcion in menu.obtener_unidades():
            ruta_unidad = os.path.join(ruta_base, menu.obtener_unidades()[opcion])

            mostrar_sub_menu(ruta_unidad)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    mostrar_menu()
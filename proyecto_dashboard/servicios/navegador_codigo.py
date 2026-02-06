import os

from servicios.lector_codigo import mostrar_codigo
from servicios.ejecutor_codigo import ejecutar_codigo

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
               if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts disponibles")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break
        elif opcion == '9':
            return
        else:
            try:
                index = int(opcion) - 1
                if 0 <= index < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[index])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")
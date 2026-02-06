## Descripción del Proyecto
### Corresponde a un Dashboard en Python que permite navegar por carpetas organizadas por unidades, vizualizar el contenido de scrips Python y ejecutarlos desde un menú interactivoen la consola. Diseñado específicamente para facilitar la gestión y ejecución de proyectos de forma ordenada.
## Estructura del proyecto
### El código fue siguiendo una arquitectura por capas:
### modelos: contiene las clases que representan los datos del sistema.
### servicios: agrupa la lógica funcional, como lectura y ejecución de scripts.
### main: controla el flujo principal del programa y la interaccón con el usario.
##  Funcionamiento general
### el programa inicia en main.py mostrando un menú principal, donde el usuario selecciona una unidad y luego una subcarpeta, donde se listan los scrips Python disponibles, el sistema permite visualizar el código y ejecutarlo en una nueva terminal 
## Desarrollo y refactorización
### import: permite importar modulos y archivos del proyecto
### from...import...: se utiliza para acceder a funciones o clases específicas 
### class: define modelos usando programación orientada a objetos 
### def: permite crear funciones
### if_name_=="_main_": establece el punto de entrada del programa 
### os.scandir(): recorre carpetas y archivos del sistema 
### os.path.join(): construye rutas de forma saegura 
### subprocess.Popen(): ejecuta scripts en una nueva terminal
### try/except: maneja erroes de ejecución 
### while True: controla menús interactivos 
### input(): permite la interacción con el usario
## Beneficios de la refactorización 
### Código más claro y profecional
### Fácil mantenimiento y ampliación del sistema 
### Compatible con entornos como PyCharm y ejecución multiplataforma
## Conclusión
### el proyecto fue desarrollado aplicando una correcta organización de código mediante una arquitectura por capas, lo que permitio mejorar la claridad, orden y la reutilización del sistema. La implementación de comandos propios de lenguaje Python y la documentación interna del código, facilitan su comprención, mantenimiento y uso.

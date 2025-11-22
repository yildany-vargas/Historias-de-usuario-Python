# -----------------------------------------------
# PROGRAMA DE INVENTARIO BÁSICO - SEMANA 2
# Este programa permite agregar productos, mostrar
# el inventario y calcular estadísticas sencillas.
# Usa listas, diccionarios, condicionales y bucles.
# -----------------------------------------------

# Lista donde guardaremos los productos como diccionarios
inventario = []


# --------------------------------------------------------
# FUNCIÓN 1: Agregar producto al inventario
# Pide nombre, precio y cantidad con validación de datos.
# --------------------------------------------------------
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    nombre = input("Ingresa el nombre del producto: ")

    # Validación del precio (debe ser número)
    while True:
        precio = input("Ingresa el precio: ")
        try:
            precio = float(precio)   # Intentamos convertir a número decimal
            break
        except ValueError:
            print("Error: el precio debe ser un número. Intenta de nuevo.")

    # Validación de cantidad
    while True:
        cantidad = input("Ingresa la cantidad: ")
        try:
            cantidad = int(cantidad)   # Intentamos convertir a número entero
            break
        except ValueError:
            print("Error: la cantidad debe ser un número. Intenta de nuevo.")

    # Crear el diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregarlo a la lista
    inventario.append(producto)

    print("Producto agregado exitosamente.")


# --------------------------------------------------------
# FUNCIÓN 2: Mostrar inventario completo
# Recorre la lista con un bucle for y muestra los productos.
# --------------------------------------------------------
def mostrar_inventario():
    print("\n--- INVENTARIO ACTUAL ---")

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# --------------------------------------------------------
# FUNCIÓN 3: Calcular estadísticas básicas
# Valor total = precio × cantidad (de todos los productos)
# Número total de productos registrados
# --------------------------------------------------------
def calcular_estadisticas():
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")

    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.")
        return

    valor_total = 0
    cantidad_total = 0

    for p in inventario:
        valor_total += p["precio"] * p["cantidad"]
        cantidad_total += p["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos registrados: {cantidad_total}")


# --------------------------------------------------------
# MENÚ PRINCIPAL
# Se mantiene en un bucle while hasta que el usuario elija salir.
# Maneja opciones inválidas sin cerrar el programa.
# --------------------------------------------------------
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        calcular_estadisticas()

    elif opcion == "4":
        print("¡Saliendo del programa! Gracias por usar el inventario.")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")


# --------------------------------------------------------
# COMENTARIO FINAL (OBJETIVO DE LA SEMANA)
# Esta semana aprendimos a usar condicionales (if/elif/else),
# bucles (while y for), listas y diccionarios para organizar
# información del inventario. También practicamos validación
# de datos y funciones para mantener el código ordenado.
# --------------------------------------------------------

# app.py
# Programa principal del sistema de inventario

# Importar las funciones de los otros módulos
from servicios import *
from archivos import *


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print(" SISTEMA DE INVENTARIO")
    print("="*50)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadísticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
    print("="*50)


def opcion_agregar(inventario):
    """Opción 1: Agregar un nuevo producto"""
    print("\n--- AGREGAR PRODUCTO ---")
    
    try:
        # Pedir datos al usuario
        nombre = input("Nombre del producto: ").strip()
        
        if nombre == "":
            print(" El nombre no puede estar vacío")
            return
        
        precio = float(input("Precio del producto: $"))
        cantidad = int(input("Cantidad disponible: "))
        
        # Validar que no sean negativos
        if precio < 0 or cantidad < 0:
            print(" El precio y la cantidad deben ser positivos")
            return
        
        # Agregar el producto
        agregar_producto(inventario, nombre, precio, cantidad)
        print(f" Producto '{nombre}' agregado correctamente")
    
    except ValueError:
        print(" Error: Debes ingresar números válidos para precio y cantidad")


def opcion_buscar(inventario):
    """Opción 3: Buscar un producto por nombre"""
    print("\n--- BUSCAR PRODUCTO ---")
    
    nombre = input("Nombre del producto a buscar: ").strip()
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        print("\n Producto encontrado:")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Cantidad: {producto['cantidad']}")
    else:
        print(f" No se encontró el producto '{nombre}'")


def opcion_actualizar(inventario):
    """Opción 4: Actualizar precio y/o cantidad de un producto"""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    nombre = input("Nombre del producto a actualizar: ").strip()
    
    # Verificar que existe
    if not buscar_producto(inventario, nombre):
        print(f" No se encontró el producto '{nombre}'")
        return
    
    try:
        print("\nDeja en blanco lo que no quieras cambiar")
        
        # Pedir nuevo precio (opcional)
        precio_input = input("Nuevo precio (Enter para no cambiar): $").strip()
        nuevo_precio = float(precio_input) if precio_input != "" else None
        
        # Pedir nueva cantidad (opcional)
        cantidad_input = input("Nueva cantidad (Enter para no cambiar): ").strip()
        nueva_cantidad = int(cantidad_input) if cantidad_input != "" else None
        
        # Validar valores positivos
        if (nuevo_precio is not None and nuevo_precio < 0) or \
           (nueva_cantidad is not None and nueva_cantidad < 0):
            print(" Los valores deben ser positivos")
            return
        
        # Actualizar
        if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
            print(f" Producto '{nombre}' actualizado correctamente")
    
    except ValueError:
        print(" Error: Debes ingresar números válidos")


def opcion_eliminar(inventario):
    """Opción 5: Eliminar un producto"""
    print("\n--- ELIMINAR PRODUCTO ---")
    
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de eliminar '{nombre}'? (S/N): ").strip().upper()
    
    if confirmacion == "S":
        if eliminar_producto(inventario, nombre):
            print(f" Producto '{nombre}' eliminado correctamente")
        else:
            print(f" No se encontró el producto '{nombre}'")
    else:
        print("Operación cancelada")


def opcion_estadisticas(inventario):
    """Opción 6: Mostrar estadísticas del inventario"""
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    
    stats = calcular_estadisticas(inventario)
    
    if stats is None:
        print(" El inventario está vacío")
        return
    
    print(f"\n Total de unidades: {stats['unidades_totales']}")
    print(f" Valor total del inventario: ${stats['valor_total']:.2f}")
    print(f" Producto más caro: {stats['producto_mas_caro'][0]} (${stats['producto_mas_caro'][1]:.2f})")
    print(f" Producto con mayor stock: {stats['producto_mayor_stock'][0]} ({stats['producto_mayor_stock'][1]} unidades)")


def opcion_guardar(inventario):
    """Opción 7: Guardar inventario en CSV"""
    print("\n--- GUARDAR INVENTARIO ---")
    
    ruta = input("Nombre del archivo (ejemplo: inventario.csv): ").strip()
    
    if ruta == "":
        ruta = "inventario.csv"
    
    # Asegurar que termine en .csv
    if not ruta.endswith('.csv'):
        ruta += '.csv'
    
    guardar_csv(inventario, ruta)


def opcion_cargar(inventario):
    """Opción 8: Cargar inventario desde CSV"""
    print("\n--- CARGAR INVENTARIO ---")
    
    ruta = input("Nombre del archivo a cargar: ").strip()
    
    # Cargar productos
    productos_nuevos = cargar_csv(ruta)
    
    if productos_nuevos is None:
        return  # Hubo error al cargar
    
    if len(productos_nuevos) == 0:
        print("  No se cargó ningún producto válido")
        return
    
    # Preguntar si sobrescribir o fusionar
    print(f"\nSe cargaron {len(productos_nuevos)} productos")
    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    
    if opcion == "S":
        # Sobrescribir: vaciar inventario y agregar todos los nuevos
        inventario.clear()
        inventario.extend(productos_nuevos)
        print(f" Inventario reemplazado con {len(productos_nuevos)} productos")
    
    else:
        # Fusionar: combinar con el inventario actual
        print("\n Fusionando inventarios...")
        print("   Política: Si el producto existe, se suma la cantidad y se actualiza el precio")
        
        fusionados = fusionar_inventarios(inventario, productos_nuevos)
        nuevos = len(productos_nuevos) - fusionados
        
        print(f"   Inventario fusionado:")
        print(f"   Productos actualizados: {fusionados}")
        print(f"   Productos nuevos: {nuevos}")
        print(f"   Total en inventario: {len(inventario)}")


def main():
    """Función principal que ejecuta el programa"""
    # Crear el inventario vacío
    inventario = []
    
    print("¡Bienvenido al Sistema de Inventario! 🏪")
    
    # Bucle principal del programa
    while True:
        mostrar_menu()
        
        try:
            # Leer opción del usuario
            opcion = input("\nSelecciona una opción (1-9): ").strip()
            
            if opcion == "1":
                opcion_agregar(inventario)
            
            elif opcion == "2":
                mostrar_inventario(inventario)
            
            elif opcion == "3":
                opcion_buscar(inventario)
            
            elif opcion == "4":
                opcion_actualizar(inventario)
            
            elif opcion == "5":
                opcion_eliminar(inventario)
            
            elif opcion == "6":
                opcion_estadisticas(inventario)
            
            elif opcion == "7":
                opcion_guardar(inventario)
            
            elif opcion == "8":
                opcion_cargar(inventario)
            
            elif opcion == "9":
                print("\n ¡Hasta pronto! Gracias por usar el sistema.")
                break
            
            else:
                print(" Opción inválida. Por favor elige un número del 1 al 9")
        
        except KeyboardInterrupt:
            print("\n\n Programa interrumpido. ¡Hasta pronto!")
            break
        
        except Exception as error:
            print(f"\n Error inesperado: {error}")
            print("El programa continuará funcionando...")


# Iniciar el programa
main()
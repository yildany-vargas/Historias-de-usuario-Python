# servicios.py
# Funciones para gestionar el inventario de productos

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    
    Parámetros:
    - inventario: lista de productos (diccionarios)
    - nombre: nombre del producto (str)
    - precio: precio unitario (float)
    - cantidad: cantidad disponible (int)
    
    Retorna: True si se agregó correctamente
    """
    # Crear un nuevo producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregar el producto a la lista
    inventario.append(producto)
    return True


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en formato tabla.
    
    Parámetros:
    - inventario: lista de productos
    
    Retorna: None
    """
    if len(inventario) == 0:
        print("\n El inventario está vacío")
        return
    
    print("\n" + "="*60)
    print(" INVENTARIO DE PRODUCTOS")
    print("="*60)
    print(f"{'Producto':<25} {'Precio':>10} {'Cantidad':>10}")
    print("-"*60)
    
    # Recorrer cada producto y mostrarlo
    for producto in inventario:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        print(f"{nombre:<25} ${precio:>9.2f} {cantidad:>10}")
    
    print("="*60 + "\n")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre en el inventario.
    
    Parámetros:
    - inventario: lista de productos
    - nombre: nombre del producto a buscar (str)
    
    Retorna: el diccionario del producto si lo encuentra, o None si no existe
    """
    # Recorrer el inventario buscando el producto
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto  # Encontrado, devolver el producto
    
    return None  # No se encontró el producto


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.
    
    Parámetros:
    - inventario: lista de productos
    - nombre: nombre del producto a actualizar (str)
    - nuevo_precio: nuevo precio (float), opcional
    - nueva_cantidad: nueva cantidad (int), opcional
    
    Retorna: True si se actualizó, False si no se encontró el producto
    """
    # Buscar el producto
    producto = buscar_producto(inventario, nombre)
    
    if producto is None:
        return False  # Producto no encontrado
    
    # Actualizar solo los valores que se proporcionaron
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por su nombre.
    
    Parámetros:
    - inventario: lista de productos
    - nombre: nombre del producto a eliminar (str)
    
    Retorna: True si se eliminó, False si no se encontró
    """
    # Buscar el producto
    producto = buscar_producto(inventario, nombre)
    
    if producto is None:
        return False
    
    # Eliminar el producto de la lista
    inventario.remove(producto)
    return True


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario completo.
    
    Parámetros:
    - inventario: lista de productos
    
    Retorna: diccionario con estadísticas (unidades_totales, valor_total,
             producto_mas_caro, producto_mayor_stock)
    """
    if len(inventario) == 0:
        return None
    
    # Calcular unidades totales
    unidades_totales = 0
    for producto in inventario:
        unidades_totales += producto["cantidad"]
    
    # Calcular valor total usando una función lambda
    calcular_subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = 0
    for producto in inventario:
        valor_total += calcular_subtotal(producto)
    
    # Encontrar producto más caro
    producto_mas_caro = inventario[0]
    for producto in inventario:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
    
    # Encontrar producto con mayor stock
    producto_mayor_stock = inventario[0]
    for producto in inventario:
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto
    
    # Crear tupla con las estadísticas
    estadisticas = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }
    
    return estadisticas
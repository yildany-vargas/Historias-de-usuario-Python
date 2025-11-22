# archivos.py
# Funciones para guardar y cargar inventario en formato CSV

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    
    Parámetros:
    - inventario: lista de productos
    - ruta: nombre/ruta del archivo CSV (str)
    - incluir_header: si se incluye encabezado (bool)
    
    Retorna: True si se guardó correctamente, False si hubo error
    """
    # Verificar que el inventario no esté vacío
    if len(inventario) == 0:
        print("\n Error: El inventario está vacío. No hay nada que guardar.")
        return False
    
    try:
        # Abrir el archivo en modo escritura
        with open(ruta, 'w', encoding='utf-8') as archivo:
            
            # Escribir encabezado si se solicita
            if incluir_header:
                archivo.write("nombre,precio,cantidad\n")
            
            # Escribir cada producto en una línea
            for producto in inventario:
                nombre = producto["nombre"]
                precio = producto["precio"]
                cantidad = producto["cantidad"]
                
                # Crear la línea CSV
                linea = f"{nombre},{precio},{cantidad}\n"
                archivo.write(linea)
        
        print(f"\n Inventario guardado en: {ruta}")
        return True
    
    except PermissionError:
        print(f"\n Error: No tienes permisos para escribir en '{ruta}'")
        return False
    
    except Exception as error:
        print(f"\n Error al guardar el archivo: {error}")
        return False


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV.
    
    Parámetros:
    - ruta: nombre/ruta del archivo CSV (str)
    
    Retorna: lista de productos cargados (puede estar vacía si hubo muchos errores)
    """
    productos = []
    filas_invalidas = 0
    
    try:
        # Abrir el archivo en modo lectura
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # Verificar que el archivo no esté vacío
        if len(lineas) == 0:
            print("\n Error: El archivo está vacío")
            return None
        
        # Leer la primera línea como encabezado
        encabezado = lineas[0].strip()
        
        # Validar que el encabezado sea correcto
        if encabezado != "nombre,precio,cantidad":
            print("\n Error: El archivo no tiene el formato correcto")
            print(f"   Se esperaba: nombre,precio,cantidad")
            print(f"   Se encontró: {encabezado}")
            return None
        
        # Procesar cada línea después del encabezado
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            
            # Saltar líneas vacías
            if linea == "":
                continue
            
            # Separar la línea por comas
            partes = linea.split(',')
            
            # Validar que tenga exactamente 3 columnas
            if len(partes) != 3:
                filas_invalidas += 1
                continue
            
            try:
                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])
                
                # Validar que precio y cantidad no sean negativos
                if precio < 0 or cantidad < 0:
                    filas_invalidas += 1
                    continue
                
                # Crear el producto y agregarlo a la lista
                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto)
            
            except ValueError:
                # Error al convertir precio o cantidad
                filas_invalidas += 1
                continue
        
        # Mostrar resumen
        print(f"\n Archivo leído correctamente")
        print(f"   Productos cargados: {len(productos)}")
        if filas_invalidas > 0:
            print(f"     Filas inválidas omitidas: {filas_invalidas}")
        
        return productos
    
    except FileNotFoundError:
        print(f"\n Error: El archivo '{ruta}' no existe")
        return None
    
    except UnicodeDecodeError:
        print(f"\n Error: El archivo no tiene el formato de texto correcto")
        return None
    
    except Exception as error:
        print(f"\n Error al leer el archivo: {error}")
        return None


def fusionar_inventarios(inventario_actual, productos_nuevos):
    """
    Fusiona productos nuevos con el inventario actual.
    Política: Si el nombre existe, suma la cantidad y actualiza el precio.
    
    Parámetros:
    - inventario_actual: lista de productos existentes
    - productos_nuevos: lista de productos a fusionar
    
    Retorna: número de productos fusionados
    """
    from servicios import buscar_producto
    
    productos_fusionados = 0
    
    for producto_nuevo in productos_nuevos:
        nombre = producto_nuevo["nombre"]
        
        # Buscar si ya existe
        producto_existente = buscar_producto(inventario_actual, nombre)
        
        if producto_existente:
            # Ya existe: sumar cantidad y actualizar precio
            producto_existente["cantidad"] += producto_nuevo["cantidad"]
            producto_existente["precio"] = producto_nuevo["precio"]
            productos_fusionados += 1
        else:
            # No existe: agregar como nuevo
            inventario_actual.append(producto_nuevo)
    
    return productos_fusionados
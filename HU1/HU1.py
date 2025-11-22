##############################################################
#SEMANA 1 – Fundamentos y operaciones básicas del inventario # 
##############################################################

# ============================================================
# ===============   TASK 1 – DIAGRAMA DE FLUJO   =============
# ============================================================

# ============================================================
# ===========   TASK 2 – ENTRADA DE DATOS (PYTHON)  ==========
# ============================================================

# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio y validar que sea número
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar la cantidad y validar que sea un entero
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: La cantidad debe ser un número entero válido.")


# ============================================================
# =======   TASK 3 – OPERACIÓN MATEMÁTICA (COSTO TOTAL)  ======
# ============================================================

costo_total = precio * cantidad


# ============================================================
# =====   TASK 4 – MOSTRAR LOS RESULTADOS EN CONSOLA   =======
# ============================================================

print("\n--- Resumen del producto registrado ---")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


# ============================================================
# ========   TASK 5 – DOCUMENTACIÓN DEL CÓDIGO   =============
# ============================================================
# Este programa permite registrar un producto para el inventario.
# Solicita nombre, precio y cantidad, validando que los datos
# ingresados sean correctos. Luego calcula el costo total
# multiplicando precio por cantidad y muestra el resultado final.
##############################################################

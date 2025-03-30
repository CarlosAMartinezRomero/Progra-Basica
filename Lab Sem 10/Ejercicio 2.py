# Diccionario que almacenará los productos.
# La clave será el nombre del producto y el valor otro diccionario con sus datos.
inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe en el inventario. Puede actualizarlo mediante otra opción.")
        return
    categoria = input("Ingrese la categoría del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
    except ValueError:
        print("Precio o cantidad no válidos. Intente nuevamente.")
        return
    inventario[nombre] = {
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
        }
    print(f"Producto '{nombre}' agregado exitosamente.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print("Producto no encontrado.")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Información del producto '{nombre}':")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Precio: {datos['precio']}")
        print(f"  Cantidad: {datos['cantidad']}")
    else:
        print("Producto no encontrado.")

def mostrar_productos_ordenados():
    if not inventario:
        print("El inventario está vacío.")
        return
    # Crear una lista de tuplas (nombre, datos) y ordenar por precio
    productos_ordenados = sorted(inventario.items(), key=lambda item: item[1]["precio"])
    print("Productos ordenados por precio (menor a mayor):")
    for nombre, datos in productos_ordenados:
        print(f"Producto: {nombre}")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Precio: {datos['precio']}")
        print(f"  Cantidad: {datos['cantidad']}")
        print("-" * 30)
# Menu para gestionar los productos
def menu():
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar todos los productos ordenados por precio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_productos_ordenados()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Nos volveremos a ver!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutamos el menú principal
if __name__ == "__main__":
    menu()

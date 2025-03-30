# Lista que almacenará los contactos
agenda = []

# Permite agregar un nuevo contacto a la agenda.
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ").strip()
    numero = input("Ingrese el número de teléfono: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")

# Busca contactos cuyo nombre contenga el término ingresado y muestra sus detalles.
def buscar_contacto():
    busqueda = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrados = [contacto for contacto in agenda if busqueda in contacto[0].lower()]
    
    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
    else:
        print("Contactos encontrados:")
        for contacto in encontrados:
            print(f"Nombre: {contacto[0]}")
            print(f"  Número: {contacto[1]}")
            print(f"  Correo: {contacto[2]}")
            print("-" * 30)

#Lista todos los contactos en orden alfabético por nombre.
def listar_contactos():
    if not agenda:
        print("La agenda está vacía.")
        return
    
    # Ordenamos la agenda por el nombre (primer elemento de la tupla), sin distinguir mayúsculas y minúsculas
    agenda_ordenada = sorted(agenda, key=lambda contacto: contacto[0].lower())
    
    print("Listado de contactos (orden alfabético):")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}")
        print(f"  Número: {contacto[1]}")
        print(f"  Correo: {contacto[2]}")
        print("-" * 30)

#Menú para gestionar la agenda de contactos.
def menu():
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("Saliendo de la agenda. ¡Hasta la vista!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutamos el menú principal
if __name__ == "__main__":
    menu()

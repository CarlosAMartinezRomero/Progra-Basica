# Llamamos a las funciones 
import conversor

# Menu de selección para que el usuario elija la converción que desea
def menu():
    while True:
        print("\n--- Conversiones ---")
        print("1. Convertir Kilómetros a Millas")
        print("2. Convertir Celsius a Fahrenheit")
        print("3. Convertir Litros a Galones")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                km = float(input("Ingrese la cantidad de kilómetros: "))
                millas = conversor.kilometros_a_millas(km)
                print(f"{km} km equivalen a {millas:.4f} millas.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif opcion == "2":
            try:
                # Reemplazamos la coma por punto para evitar errores en la conversión
                entrada_celsius = input("Ingrese la temperatura en Celsius: ").replace(',', '.')
                celsius = float(entrada_celsius)
                fahrenheit = conversor.celsius_a_fahrenheit(celsius)
                print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == "3":
            try:
                litros = float(input("Ingrese la cantidad de litros: "))
                galones = conversor.litros_a_galones(litros)
                print(f"{litros} litros equivalen a {galones:.4f} galones.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        elif opcion == "4":
            print("Saliendo del convertidor. ¡Bye!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

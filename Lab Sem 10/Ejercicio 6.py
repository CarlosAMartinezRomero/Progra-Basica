class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        print("Información del vehículo:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Año: {self.año}")
        print(f"  Precio: ${self.precio:.2f}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, puertas):
        super().__init__(marca, modelo, año, precio)
        self.puertas = puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"  Número de puertas: {self.puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"  Cilindrada: {self.cilindrada} cc")

# Ejemplo del funcionamineto
def main():
    # Crear una instancia de Automovil
    auto = Automovil("Toyota", "Corolla", 2022, 23000, 4)
    auto.mostrar_informacion()
    print("-" * 40)
    
    # Crear una instancia de Motocicleta
    moto = Motocicleta("Honda", "CBR500R", 2021, 7000, 500)
    moto.mostrar_informacion()
main()
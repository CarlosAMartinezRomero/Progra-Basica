import math

#Volumenes
def volumen_cubo(lado):
    return lado ** 3

def volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

def volumen_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura

def volumen_cono(radio, altura):
    return math.pi * (radio ** 2) * altura * (1/3)

#Areas
def area_cubo(lado):
    return lado ** 2

def area_esfera(radio):
    return 4 * math.pi * (radio ** 2)

def area_cilindro(radio, altura):
    return math.pi * radio  * (radio + altura) * 2

def area_cono(radio, altura):
    generatriz = math.sqrt(radio ** 2 + altura ** 2) 
    return math.pi * radio * (radio + generatriz)
        

def main():
    print("Calculadora de Volumen y Area")
    print ("1. Cubo")
    print ("2. Esfera")
    print ("3. Cilindro")
    print ("4. Cono")

    opcion = int(input("Seleccione una figura (1-4): "))

    if opcion == 1:
        lado = float(input("Ingrese la longitud del lado del cubo: "))
        print(f"Volumen del cubo: {volumen_cubo(lado)}")
        print(f"Area del cubo: {area_cubo(lado)}")

    elif opcion == 2:
        radio = float(input("Ingrese el radio de la esfera: "))
        print(f"Volumen de la esfera: {volumen_esfera(radio)}")
        print(f"Areal de la esfera: {area_esfera(radio)}")

    elif opcion == 3:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilinddro: "))
        print(f"Volumen del cilindro: {volumen_cilindro(radio, altura)}")
        print(f"Area del cilindro: {area_cilindro(radio, altura)}")

    elif opcion == 4:
        radio = float(input("Ingrese el radio del cono: "))
        altura = float(input("Ingrese la altura del cono: "))
        print(f"Volumen del cono: {volumen_cono(radio, altura)}")
        print(f"Area del cono: {area_cono(radio, altura)}")

    else:
        print("Opcion no valida. Intente de nuevo.")
main()        


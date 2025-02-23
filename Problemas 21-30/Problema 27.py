def conversion_mm_cm(mm):
    return mm / 10

def convercion_cm_m(cm):
    return cm / (10**2)

def conversion_m_km(m):
    return m / (10**3)

def conversion_g_kg(g):
    return g / (10**3)

def conversion_kg_tn(kg):
    return kg / (10**3)

def main():
    print("Conversiones")
    print("1. mm a cm")
    print("2. cm a m")
    print("3. m a km")
    print("4. g a kg")
    print("5. kg a tn")

    option = int(input("Seleccione la conversion"))

    if option == 1:
        mm = float(input("Ingrese los Milimetros: "))
        print(f"En centimetros son: {conversion_mm_cm(mm)}")

    elif option == 2:
        cm = float(input("Ingrese los Centimetros: "))
        print(f"En metros son: {convercion_cm_m(cm)}")

    elif option == 3:
        m = float(input("Ingrese los Metros: "))
        print(f"En kilometros son: {conversion_m_km(m)}")

    elif option == 4:
        g = float(input("Ingrese los Gramos: "))
        print(f"En kilogramos son: {conversion_g_kg(g)}")

    elif option == 5:
        kg = float(input("Ingrese los Kilogramos: "))
        print(f"En toneladas son: {conversion_kg_tn(kg)}")

main()
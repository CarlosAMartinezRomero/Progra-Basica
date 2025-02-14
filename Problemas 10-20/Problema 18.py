import math
import cmath


def resolver_ecuacion_cuadratica(a, b, c):
    

    if a == 0:
        return "No es una ecuación cuadrática si a = 0."

    Discriminante = b**2-4*a*c

    if Discriminante > 0:
        x1 = (-b + math.sqrt(Discriminante))/(2*a)
        x2 = (-b - math.sqrt(Discriminante))/(2*a)
        return f"Dos soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}"
    
    elif Discriminante == 0:
        x = -b/(2*a)
        return f"Una solucion real (doble): x = {x:.2f}"
    
    elif Discriminante < 0:
         x1 = (-b + cmath.sqrt(Discriminante)) / (2 * a)
         x2 = (-b - cmath.sqrt(Discriminante)) / (2 * a)
         return f"Dos soluciones complejas: x1 = {x1}, x2 = {x2}"



def main():
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print(resultado)
    
    
main()



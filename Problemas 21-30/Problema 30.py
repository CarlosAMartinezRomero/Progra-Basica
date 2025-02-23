def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def main():

    numero = int(input("Ingrese un número: "))

    resultado = factorial(numero)

    print(f"El factorial de {numero} es {resultado}")

main()

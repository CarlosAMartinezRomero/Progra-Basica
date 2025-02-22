import random

def main():

    resultado = random.choice(["aguila", "sol"])

    print("Cara de la moneda:", resultado)

    numero = random.randint(1,6)

    print("Resultado del dado:", numero)

main()
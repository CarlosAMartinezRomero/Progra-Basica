def main():

    texto = input("ingrese un texto: ").lower()
    vocales = "aeiou"
    numvocales = 0
    numconsonantes = 0

    for letra in texto:
        if letra.isalpha:
            if letra in vocales:
                numvocales += 1
            else:
                numconsonantes += 1
    print(f"las vocales son {numvocales} y las consonantes son {numconsonantes}")
    
main()
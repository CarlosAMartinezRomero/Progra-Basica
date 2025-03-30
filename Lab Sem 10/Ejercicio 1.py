def main():
    
    # Solicitamos al usuario que ingrese un texto
    texto = input("Ingresa un texto: ")

    # Convertimos el texto a minúsculas 
    texto = texto.lower()

    # Separar el texto en palabras
    palabras = texto.split()

    # Número total de palabras
    total_palabras = len(palabras)

    # Conjunto de palabras únicas
    palabras_unicas = set(palabras)
    total_palabras_unicas = len(palabras_unicas)

    # Frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # Determinamos la palabra más frecuente y cuántas veces aparece
    palabra_mas_frecuente = None
    max_frecuencia = 0
    for palabra, conteo in frecuencia.items():
        if conteo > max_frecuencia:
            max_frecuencia = conteo
            palabra_mas_frecuente = palabra

    # Mostramos el resumen con los datos
    print("\nResumen del análisis:")
    print("Número total de palabras:", total_palabras)
    print("Número de palabras únicas:", total_palabras_unicas)
    print("Frecuencia de cada palabra:")
    for palabra, conteo in frecuencia.items():
        print(f"  {palabra}: {conteo}")
    print("La palabra más frecuente es '{}' y aparece {} veces.".format(palabra_mas_frecuente, max_frecuencia))

main()
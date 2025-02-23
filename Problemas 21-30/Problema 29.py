import random
def main():
    random.seed(42)  
    edades = [random.randint(18, 70) for _ in range(100)]

    media = sum(edades) / len(edades)

    edades_ordenadas = sorted(edades)
    n = len(edades)
    if n % 2 == 0:
        mediana = (edades_ordenadas[n // 2 - 1] + edades_ordenadas[n // 2]) / 2
    else:
        mediana = edades_ordenadas[n // 2]

    suma_cuadrados = sum((x - media) ** 2 for x in edades)
    desviacion_estandar = (suma_cuadrados / len(edades)) ** 0.5

    minimo = min(edades)
    maximo = max(edades)

    print(f"Estadísticas:\n")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación Estándar: {desviacion_estandar}")
    print(f"Valor Mínimo: {minimo}")
    print(f"Valor Máximo: {maximo}")

main()
def calcular_estadisticas(*args):
    
    # Convertir los argumentos a una lista y asegurarse de que haya al menos un número
    numeros = list(args)
    n = len(numeros)
    if n == 0:
        return None, None, None

    # Función lambda para calcular el promedio
    promedio = (lambda nums: sum(nums) / len(nums))(numeros)

    # Calcular la mediana
    numeros_ordenados = sorted(numeros)
    if n % 2 == 1:
        mediana = numeros_ordenados[n // 2]
    else:
        mediana = (numeros_ordenados[(n // 2) - 1] + numeros_ordenados[n // 2]) / 2

    # Calcular la desviación estándar 
    # Usamos lambda para calcular la suma de las diferencias al cuadrado
    suma_diferencias = (lambda nums, prom: sum((x - prom) ** 2 for x in nums))(numeros, promedio)
    desviacion_estandar = (suma_diferencias / n) ** 0.5

    return promedio, mediana, desviacion_estandar

# Función principal para solicitar datos al usuario y mostrar resultados
def main():
    entrada = input("Ingrese una lista de números separados por comas: ")
    try:
        # Convertir la entrada a una lista de números (float)
        lista_numeros = [float(num.strip()) for num in entrada.split(",") if num.strip()]
    except ValueError:
        print("Error: Asegúrese de ingresar números separados por comas.")
        return

    if not lista_numeros:
        print("No se ingresaron números.")
        return

    # Obtenemos el promedio, la mediana y la desviacion estandar
    prom, med, desv = calcular_estadisticas(*lista_numeros)
    print("\nResultados:")
    print(f"Promedio: {prom}")
    print(f"Mediana: {med}")
    print(f"Desviación estándar: {desv}")

# Ejecutamos el menú
if __name__ == "__main__":
    main()

import random

def generar_lista(tamano, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(tamano)]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def main():
    tamano = int(input("Ingrese el tamaño de la lista: "))
    minimo = int(input("Ingrese el valor mínimo: "))
    maximo = int(input("Ingrese el valor máximo: "))
    
    lista = generar_lista(tamano, minimo, maximo)
    print("Lista generada:", lista)
    
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)
    
    objetivo = int(input("Ingrese el número a buscar: "))
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    
    if resultado != -1:
        print(f"El número {objetivo} se encuentra en la posición {resultado}.")
    else:
        print(f"El número {objetivo} no está en la lista.")

if __name__ == "__main__":
    main()

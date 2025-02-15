def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda - derecha)//2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1 

def main():
    lista = [1, 2 ,3 ,4 ,5 ,6 ,7 , 8]
    resultado = busqueda_lineal(lista, 8)
    print(f"El valor se encuentra en el índice: {resultado}")
    
    lista_ordenada = [1, 3, 5, 7, 8, 10]
    resultado = busqueda_binaria(lista_ordenada, 8)
    print(f"El valor se encuentra en el índice: {resultado}")

main()


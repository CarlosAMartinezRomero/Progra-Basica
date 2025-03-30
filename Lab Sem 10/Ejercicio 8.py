def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def main():
    lista = list(map(int, input("Ingrese los números separados por espacios: ").split()))
    print("Lista ingresada:", lista)
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()

def main():

    matriz1 = [
    [1,2,5],
    [3,4,5],
    [8,6,3]
    ]

    matriz2 = [
        [9,6,7],
        [0,3,4],
        [5,2,1]
    ]
    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

    for fila in resultado:
        print(fila)

main()

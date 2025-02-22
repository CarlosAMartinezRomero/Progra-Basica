def main():
    serie1 = range(1,11)
    serie2 = range(1,20)

    suma_elemento_a_elemento = [a + b for a,b in zip(serie1,serie2)]
    print(suma_elemento_a_elemento)
main()
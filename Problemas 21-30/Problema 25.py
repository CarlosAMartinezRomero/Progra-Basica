from collections import Counter

def main():

    edades = [4,5,6,7,8,9,10,11,12,23,24,25,26,27,49,47,56,98,76,56,57,87,76,84]

    bins = [0,10,20,30,50,60,70,90]

    histograma = Counter((min(bins, key=lambda x: abs(x-edad)) for edad in edades))

    for rango in bins:
        print(f"{rango}-{rango+10}: {'#' * histograma[rango]}")

main()
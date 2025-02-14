def main():
    
    year = int(input("ingrese el año: "))    
   
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
       print("el año es bisiesto") 
    else: 
        print("el año no es bisiesto")

main()
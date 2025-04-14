import math
def line():
    coeficiente_A= float(input("Ingrese el coeficiente A: "))
    coeficiente_B= float(input("Ingrese el coeficiente B: "))
    coeficiente_X1= float(input("Ingrese el coeficiente X1: "))
    coeficiente_X2= float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:", coeficiente_A)
    print("El coeficiente B de su ecuación de la recta es:", coeficiente_B)
    print("El coeficiente X1 de su ecuación de la recta es:", coeficiente_X1)
    print("El coeficiente X2 de su ecuación de la recta es:", coeficiente_X2)
    print(" ")    
    print("Para la siguiente ecuación:")
    print(f"\tY = {coeficiente_A}X + {coeficiente_B}")
    print(" ")  
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coeficiente_X1}, {(coeficiente_A*coeficiente_X1) + coeficiente_B})")
    print(f"\tP2 ({coeficiente_X2}, {(coeficiente_A*coeficiente_X2) + coeficiente_B})")
    print(" ")    
    Y1 = coeficiente_A * coeficiente_X1 + coeficiente_B
    Y2 = coeficiente_A * coeficiente_X2 + coeficiente_B
    distancia = math.sqrt((coeficiente_X2 - coeficiente_X1)**2 + (Y2 - Y1)**2)
    print(f"La distancia entre ellos es: {distancia}")

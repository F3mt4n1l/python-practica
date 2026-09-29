nota = float(input("ingrese la nota( 0 para salir):  "))
while nota != 0:
    if nota >= 4.5:
        print("excelente")
    elif nota >= 3.0:
        print("aprobado")
    else:
        print("reprobado")
    nota = float(input("ingrese la nota( 0 para salir):  "))
continuar = "s"
while continuar == "s":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    print("La suma es:", numero1 + numero2)
    print("La resta es:", numero1 - numero2)
    print("La multiplicación es:", numero1 * numero2)
    if numero2 != 0:
        print("La división es:", round(numero1 / numero2, 2))
    else:
        print("No se puede dividir por cero")
    continuar = input("¿Desea continuar? (s/n): ")
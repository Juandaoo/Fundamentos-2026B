numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print("Los numeros ingresados son: ", numero1, "y", numero2)

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("Ingrese la operacion que desea hacer: ")

if opcion == "1":
    suma = numero1 + numero2
    print("La suma de los numeros es: ", suma)
elif opcion == "2":
    resta = numero1 - numero2
    print("La resta de los numeros es: ", resta)
elif opcion == "3":
    multiplicacion = numero1 * numero2
    print("La multiplicacion de los numeros es: ", multiplicacion)
elif opcion == "4":
    division = numero1 / numero2
else:

    print("Opcion no valida")


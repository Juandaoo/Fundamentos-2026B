print("Calcular el area y perimetro de figuras ")
print("1. Cuadrado")
print("2. Rectangulo")
print("3. Triangulo")
print("4. Circulo")
opcion = input("Ingrese el numero de la figura que deseas calcular: ")

if opcion == "1":
    lado = float(input("Ingrese el valor del lado del cuadrado que nesesita:"))
    area = lado * lado
    perimetro = lado * 4
    print("El area del cuadrado es: ", area)
    print("El perimetro del cuadrado es: ", perimetro)
elif opcion == "2":
    base = float(input("Ingrese el valor de la base del rectangulo que nesesita:"))
    altura = float(input("Ingrese el valor de la altura del rectangulo que nesesita:"))
    area = base * altura
    perimetro = (base + altura) * 2
    print("El area del rectangulo es: ", area)
    print("El perimetro del rectangulo es: ", perimetro)
elif opcion == "3":
    base = float(input("Ingrese el valor de la base del triangulo que nesesita:"))
    altura = float(input("Ingrese el valor de la altura del triangulo que nesesita:"))
    area = (base * altura) / 2
    perimetro = base + altura + ((base ** 2 + altura ** 2) ** 0.5)
    print("El area del triangulo es: ", area)
    print("El perimetro del triangulo es: ", perimetro)
elif opcion == "4":
    radio = float(input("Ingrese el valor del radio del circulo que nesesita:"))
    area = 3.1416 * (radio ** 2)
    perimetro = 2 * 3.1416 * radio
    print("El area del circulo es: ", area)
    print("El perimetro del circulo es: ", perimetro)

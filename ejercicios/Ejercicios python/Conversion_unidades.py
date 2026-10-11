print("Calculadora de conversion de unidades:")
print("Seleccione la conversion que quiere realizar: ")
print("1. De temperaura: Celsius a kelvin")
print("2. De temperaura: Celsius a Fahrenheit")
print("3. De Distancia de : kilometros a millas")
print("4. De peso: de kilogramos a libras")
print("5. De monedas: de dolares a pesos colombianos")

opcion = int(input("Ingrese el numero de la conversion que desea realizar: "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura medida en Celsius: "))
    kelvin = celsius + 273.15
    print(f"La temperatura en Kelvin es: ", kelvin)
if opcion == 2:
    celsius = float(input("Ingrese la temperatura medida en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en Fahrenheit es: fahrenheit", fahrenheit)
if opcion == 3:
    kilometros = float(input("Ingrese la distancia medida en kilometros: "))
    millas = kilometros * 0.621371
    print(f"La distancia en millas es: ", millas)
if opcion == 4:
    kilogramos = float(input("Ingrese el peso medido en kilogramos: "))
    libras = kilogramos * 2.20462
    print(f"El peso en libras es: ", libras)
if opcion == 5:
    dolares = float(input("Ingrese la cantidad de dolares: "))
    pesos_colombianos = dolares * 4000
    print(f"La cantidad en pesos colombianos es: ", pesos_colombianos)

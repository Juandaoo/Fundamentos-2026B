segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"El tiempo ingresado es: {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
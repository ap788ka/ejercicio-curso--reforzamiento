#Convertidor de temperatura 
celsius = float(input("Temperatura en °C: "))
print("1. Farenheit/n2. Kelvin")
opcion = int(input("Eloge opción: "))
match opcion:
    case 1:
        resultado = celsius * 9/5 + 32
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("Opción Inválida")
if resultado is not None:
    print("Convertido:", resultado, unidad)

def leer_temperaturas():
    temperaturas = []
    for i in range(10):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura en °C del paciente {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Ingrese un número válido para la temperatura.")
    
    print("\nTemperaturas registradas en grados Celsius:")
    for i, temp in enumerate(temperaturas, 1):
        print(f"Paciente {i}: {temp} °C")

leer_temperaturas()

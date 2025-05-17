def calcular_promedio_toneladas():
    toneladas = []
    for i in range(12):
        while True:
            try:
                cantidad = float(input(f"Ingrese la cantidad de toneladas del mes {i + 1}: "))
                toneladas.append(cantidad)
                break
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")
    
    promedio = sum(toneladas) / len(toneladas)
    print(f"\nEl promedio de toneladas mensuales en 2024 es: {promedio:.2f} toneladas")

calcular_promedio_toneladas()
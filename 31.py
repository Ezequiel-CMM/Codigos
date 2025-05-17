def obtener_numeros_unicos(cantidad):
    numeros = set()
    while len(numeros) < cantidad:
        try:
            num = int(input(f"Ingrese un número ({len(numeros) + 1}/{cantidad}): "))
            if num in numeros:
                print("El número ya fue ingresado, ingrese uno diferente.")
            else:
                numeros.add(num)
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
    return list(numeros)

def calcular_mayor_menor():
    numeros = obtener_numeros_unicos(20)
    mayor = max(numeros)
    menor = min(numeros)
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")


calcular_mayor_menor()

# Pedir al usuario que ingrese la temperatura en grados Fahrenheit
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

# Convertir la temperatura a Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Mostrar el resultado
print(f"La temperatura en Celsius es: {celsius}")


iva = 16
precioBase = float(input("Introduce el precio del producto: "))
total = precioBase * (1 + iva / 100)
iva_calculado = precioBase * (iva / 100)
print(f"El precio del producto es: {precioBase}")
print(f"El IVA es: {iva_calculado}")
print(f"El total a pagar (producto + IVA) es: {total}")

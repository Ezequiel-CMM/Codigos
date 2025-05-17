def leer_caracteres():
    vector = ["" for _ in range(5)]
    for i in range(5):
        while True:
            caracteres = input(f"Ingrese 10 caracteres para la posición {i + 1}: ")
            if len(caracteres) == 10:
                vector[i] = caracteres
                break
            else:
                print("Debe ingresar exactamente 10 caracteres.")
    
    print("Vector resultante:")
    for i, valor in enumerate(vector):
        print(f"Posición {i + 1}: {valor}")

leer_caracteres()
num_alumnos = 38

suma_calificaciones = 0


for alumno in range(1, num_alumnos + 1):
    
    calificacion = float(input(f"Ingrese la calificación final del alumno {alumno}: "))
    
    
    suma_calificaciones += calificacion


promedio = suma_calificaciones / num_alumnos


print(f"El promedio general de los {num_alumnos} alumnos es: {promedio:.2f}")

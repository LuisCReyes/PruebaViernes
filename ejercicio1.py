""" Ejercicio 1: Registro de asistencia académica
Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de
la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por
sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por
sección, así como el total general de la semana. """

# Registro de asistencia académica UAM

secciones = 3
estudiantes_por_seccion = 6
dias = 5

# Matriz para almacenar las asistencias
asistencias = [[0 for _ in range(estudiantes_por_seccion)] for _ in range(secciones)]

# Recorrer secciones
for s in range(secciones):
    print(f"\n=== Sección {s+1} ===")
    total_seccion = 0
    # Recorrer días
    for d in range(dias):
        print(f"\nDía {d+1}")
        # Recorrer estudiantes
        for e in range(estudiantes_por_seccion):
            while True:
                try:
                    asistencia = int(input(f"Ingrese [1] si el estudiante {e+1} asistió o [0] si no asistió: "))
                    if asistencia not in [0, 1]:
                        print("Error: Solo se acepta [1] (asistió) o [0] (no asistió). Intente de nuevo.")
                        continue
                    asistencias[s][e] += asistencia
                    break
                except ValueError:
                    print("Entrada no válida. Ingrese 1 o 0.")
    
    # Sección procesada
    print(f"\nTotal de asistencias en la sección {s+1} hasta ahora: {sum(asistencias[s])}")

# Mostrar resumen por sección
print("\n=== Resumen de Asistencias por Sección ===")
total_general = 0
for s in range(secciones):
    total_seccion = sum(asistencias[s])
    print(f"Sección {s+1}: {total_seccion} asistencias")
    total_general += total_seccion

# Mostrar total general
print(f"\nTotal general de asistencias en la semana: {total_general}")

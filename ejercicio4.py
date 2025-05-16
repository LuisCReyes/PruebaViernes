#Monitoreo del consumo energético

#Definición de variables
edificios_campus = int(input("Ingrese el número de edificios del campus: "))

consumo_neto_energetico = 0

#Validación de la cantidad de edificios
for edificios in range(edificios_campus):
    print(f"\nEdificios en el campus {edificios + 1}: ")
    
    #Validación de la cantidad de días de la semana
    for días_semana in range(1, 8):
        día_turno = int(input(f"Ingrese el día de la semana: "))
        consumo_edificio = 0
        #Validación del día de la semana
        if día_turno < 1 or día_turno > 7:
            print("El día de la semana no es correcto, por favor ingrese un número entre 1 y 7.")
            continue
        #Validación del consumo energético por turno
        consumo_mañana = float(input(f"¿Cuánto fue el consumo energía del edificio #{edificios + 1} por la mañana? "))
        consumo_tarde = float(input(f"¿Cuánto fue el consumo de energía del edificio #{edificios + 1} por la tarde? "))
        consumo_noche = float(input(f"¿Cuánto fue el consumo de energía del edificio #{edificios + 1} por la noche? "))

        #Suma de los consumos por turno
        total_turnos = consumo_mañana + consumo_tarde + consumo_noche
        print(f"El total del día #{día_turno} es igual a {total_turnos:.2f} kilovatios ")
        consumo_edificio += total_turnos
    
    #Suma del consumo energético por edificio    
    promedio_edificio = consumo_edificio / 7
    print(f"\nEl consumo energético total del edificio #{edificios + 1} es de {consumo_edificio:.2f} kilovatios ")
    print(f"El consumo energético promedio semanal del edificio #{edificios + 1} es de {promedio_edificio:.2f} kilovatios ")

    # Para poder sumar el total general
    consumo_neto_energetico += consumo_edificio  

#Total del consumo energético de todos los edificios
print(f"\nEl consumo energetico total de los #{edificios_campus} edificios es de {consumo_neto_energetico:.2f} kilovatios ")
consumo_promedio_semanal = consumo_neto_energetico / (edificios_campus * 7)
print(f"El consumo energetico promedio por semana es {consumo_promedio_semanal:.2f} kilovatios ")
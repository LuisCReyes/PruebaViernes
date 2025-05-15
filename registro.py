#Ejercicio 2: Uso de computadoras en laboratorios 
#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del 
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora 
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con 
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras 
#ocupadas y libres por laboratorio. 
print("ESTADO DE LAS COMPUTADORAS DE LABORATORIO 1 Y 2")
print(f"==++=="*20)
labortorio1_libre = 0
labortorio1_ocupada = 0
labortorio2_libre = 0
labortorio2_ocupada = 0
for laboratorio in range (1,3):
    print(f"INGRESE LOS EL ESTADO DE LA COMPUTADORAS EN EL LABORATORIO {laboratorio}")
    for filas in range (1, 6):
        for computadoras in range (1,5):
            while estado == "L" or estado == "O":
             estado = str(input("INGRESE EL ESTADO DE LA COMPUTADORA [L = LIBRE, O = OCUPADO]")) 
             if estado != "L" and estado != "O":  
                 print("ERROR, INGRESE EL VALOR REQUERIDO [L = LIBRE, O = OCUPADO]")
            break
        if estado == "L":
            if laboratorio == 1:
                labortorio1_libre += labortorio1_libre
            else:
                labortorio2_libre += labortorio2_libre
        else:
            if laboratorio == "O":
                labortorio1_ocupada += labortorio1_ocupada
            else:
                labortorio2_ocupada += labortorio2_ocupada

print(f"==++=="*20)
print("RESUMEN DEL ESTADO DE LA COMPUTADORA POR LABORATORIO: ")
print(f"==++=="*20)
print("LABORATORIO 1")
print(f"Computadoras libre: {labortorio1_libre}")
print(f"Computadoras ocupadas: {labortorio1_ocupada}")
print(f"==++=="*20)
print("LABORATORIO 2")
print(f"Computadoras libres: {labortorio2_libre}")
print(f"Computadoras ocupadas: {labortorio2_ocupada}")
print(f"==++=="*20)
print("FIN DEL RESUMEN")
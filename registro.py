#Ejercicio 2: Uso de computadoras en laboratorios 
#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del 
#campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora 
#se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con 
#valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras 
#ocupadas y libres por laboratorio. 

print("ESTADO DE LAS COMPUTADORAS DE LABORATORIO 1 Y 2")
print(f"==++=="*20)
labortorio1_libre = 0
labortorio1_ocupada = 0    #Contadores necesarios a la hora que ejecute el ciclo
labortorio2_libre = 0      #Cada uno de ellos corresponde a un laboratorio (ciclo) diferente
labortorio2_ocupada = 0
estado = ""
for laboratorio in range (1,3): # Se supone que todo lo de adentro se repetira hasta 2 veces, dando los laboratorios 
    print(f"INGRESE LOS EL ESTADO DE LA COMPUTADORAS EN EL LABORATORIO {laboratorio}") # Como en pseudocodigo, me permitirá distinguir el momento que acabo el primer ciclo (Laboratorio)
    for filas in range (1, 6): # Repite el ciclo de for computadoras... 4 veces
        for computadoras in range (1,5): # Como este ciclo esta bajo influencia de el anterior, se supone que serían unas 5*4 veces, es decir 20 veces
            while True: #En este trato de asegurame que estado es solo L o solo O
             estado = str(input("INGRESE EL ESTADO DE LA COMPUTADORA [L = LIBRE, O = OCUPADO]")) 
             if estado != "L" and estado != "O":  # Si ponen otro valor, les debería saltar el sig mensaje de error
                 print("ERROR, INGRESE EL VALOR REQUERIDO [L = LIBRE, O = OCUPADO]")
            break #Cuando deje d ingresar el valor equivocado, se dentedrá el cilo while (Dejara de aparecer el mensaje de error)
        if estado == "L": #Con esta condición me aseguro el uso del contador para las L
            if laboratorio == 1: # Si determina que esta en el 1er ciclo, el contaoor aumentará 
                labortorio1_libre += labortorio1_libre
            else: # Sino se cumple la condición, el contador aumentara para el segundo laboratorio
                labortorio2_libre += labortorio2_libre 
        else:
            if laboratorio == "O":
                labortorio1_ocupada += labortorio1_ocupada
            else:            # Es analogamente igual a la anterior condición, pero será para las O
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
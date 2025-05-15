Algoritmo Registro_computadora
//Ejercicio 2: Uso de computadoras en laboratorios 
//Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del 
//campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora 
//se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con 
//valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras 
//ocupadas y libres por laboratorio. 
	
	Definir laboratorio, fila, computadora como entero 
	Definir estado Como Caracter // En mi caso lo hice de tipo caracter para que el usario ingrese las letras O y L 
	Definir laboratorio1_ocupado, laboratorio1_libre, laboratorio2_ocupado, laboratorio2_libre Como Entero
	laboratorio1_ocupado = 0 //Inicio todos estos contadores para que registren individualmente cada laboratorio
	laboratorio1_libre = 0
	laboratorio2_ocupado = 0 
	laboratorio2_libre = 0 //Me perdia a la hora de probar su ejecución, por lo que para probar si podria visualizar mejor luego de decidir de cambiar el código
	
	
	Para laboratorio desde 1 hasta 2 //Iniciamkos un bucle con "Para" con la variable "laboratorio" para hacer proceso 2 veces, en toeria
		Escribir "Ingresando datos para laboratorio ", laboratorio //Cuando se ejecute la segunda vez, me avisará que ahora sera de laboratorio 2
		Para fila Desde 1 hasta 5 //Igualmente se inicia el bucle "Para" con "fila"  para que el siguiente proceso se repita 5 veces
			Para computadora desde 1 hasta 4//Es analógamente igual que el anterior, pero para "computadora"
				Repetir //Utilice en este caso el repetir  para asegurarme que esta condicion se repita hasta que el usuario ingrese el valor que le pido, "L" o "O"
					Escribir "Ingrese el estado de uso [O = Ocupado, L = Libre ]: "
					Leer estado
					Si estado <> "O" y estado <> "L" Entonces // Use este "Si" para que se ejecute la siguiente linea si los valores son difentes a los requeridos
						Escribir "Ingrese el valor requerido [O = Ocupado, L = Libre]" // Cuando no se ingrese el valor que le pedi, le saltará este mensaje
					FinSi
				Hasta Que estado == "L" o estado == "O" // Aqui daria terminado el proceso insetar y asegurarme de un correcto ajuste
				Si estado == "L" Entonces  
					Si laboratorio == 1 Entonces
						laboratorio1_libre = laboratorio1_libre + 1
					SiNo                                           //Mientras laboratorio == 1 se ejecutara este contador de las "L"  en el laboratorio 1
						laboratorio2_libre = laboratorio2_libre + 1 // Si no se cumple esa condición de laboratorio == 1 pasara a suma las "L" o las en el laboratorio 2, sabiendo el cambio de ejecución del ciclo
					FinSi
				SiNo
					si laboratorio == 1 Entonces
						laboratorio1_ocupado = laboratorio1_ocupado + 1
					SiNo                                               // Es analogomente similar para la condición similar, solamente que es para las "O" de ambos laboratorios
						laboratorio2_ocupado = laboratorio2_ocupado + 1
					FinSi
				FinSi  
			FinPara
		FinPara
	FinPara
	
	Escribir "RESUMEN:"
	Escribir  "==============================================================================================================="
	Escribir "LABORATORIO 1: "
	Escribir "Computadoras libres: ", laboratorio1_libre
	Escribir "Computadoras ocupadas: ", laboratorio1_ocupado
	Escribir  "==============================================================================================================="
	Escribir "LABORATORIO 2: "
	Escribir "Computadoras libres: ", laboratorio2_libre
	Escribir "Computadoras ocupadas: ", laboratorio2_ocupado
	Escribir  "==============================================================================================================="
	Escribir "FIN DEL RESUMEN"
FinAlgoritmo

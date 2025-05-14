Algoritmo Registro_computadora
//Ejercicio 2: Uso de computadoras en laboratorios 
//Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del 
//campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora 
//se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con 
//valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras 
//ocupadas y libres por laboratorio. 
	
	Definir laboratorio, fila, computadora como entero 
	Definir estado Como Caracter // En mi caso lo hice de tipo caracter para que el usario ingrese las letras O y L 
	
	
	
	Para laboratorio desde 1 hasta 2 //Iniciamkos un bucle con "Para" con la variable "laboratorio" para hacer proceso 2 veces, en toeria
		libre = 0 //Necesitare esto como un contador del estado de las compus
		ocupado = 0 // Igualmente acá, para el estado de ocupaod
		Para fila Desde 1 hasta 5 //Igualmente se inicia el bucle "Para" con "fila"  para que el siguiente proceso se repita 5 veces
			Para computadora desde 1 hasta 4//Es analógamente igual que el anterior, pero para "computadora"
				Repetir //Utilice en este caso el repetir  para asegurarme que el usuario ponga el valor correcto
					Escribir "Ingrese el estado de uso [O = Ocupado, L = Libre ]: "
					Leer estado
					Si estado <> "O" y estado <> "L" Entonces // Use este "Si" para que el usuario sea capaz de poner solo "O" o "L"
						Escribir "Ingrese el valor requerido [O = Ocupado, L = Libre]" // Cuando no se ingrese el valor que le pedi, le saltará este mensaje
					FinSi
				Hasta Que estado == "L" o estado == "O" // Aqui daria terminado el proceso insettar datos
				Si estado == "L" Entonces  
					libre = libre + 1  
				Sino        // De esta manera, cuando una de las 2 condiciones se cumplan el contador incrementara en 1, por eso era necesario
					ocupado = ocupado + 1  
				FinSi  
			FinPara
		FinPara
	FinPara
	
	Escribir "Resumen de laboratorio ", laboratorio
	Escribir "Computadoras libres: ", libre           // Aqui en teoría deberia mostrar el resumen de los laboratorio
	Escribir "Computadoras ocupadas: ", ocupado	
FinAlgoritmo

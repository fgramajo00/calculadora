#autor: Federico Gramajo
#Calculadora basica
import os
suma = lambda nro1, nro2: nro1+nro2
resta = lambda nro1, nro2 : nro1 - nro2
multiplicacion = lambda nro1, nro2 : nro1 * nro2
division = lambda nro1,nro2: nro1 / nro2

while True:
	print("		### CALCULADORA BASICA ###")
	print(''' 
	1. Suma de dos numero
	2. Resta de dis numeros
	3. Multiplicacion de dos numeros
	4. Division de dos numeros 
	5. Salir ''')
	print("")
	opcion = input("ingrese una opcion: ")
	if opcion == "1":	
		os.system('clear')
		nro1=int(input("ingrese nro: "))
		nro2= int(input("ingrese nro: "))
		print(f"La suma es igual a {suma(nro1,nro2)}")
		break
	if opcion == "2":
		os.system('clear')		
		nro1=int(input("ingrese nro: "))
		nro2 = int(input("ingrese nro: "))
		print(f"La resta es igual a {resta(nro1,nro2)}")
		break
	if opcion == "3":
		os.system('clear')
		nro1=int(input("ingrese nro: "))
		nro2= int(input("ingrese nro: "))
		print(f"La multiplicacion es igual a {multiplicacion(nro1,nro2)}")
		break
	if opcion =="4":
		os.system('clear')
		nro1=int(input("ingrese nro: "))
		try: 
			nro2 = int(input("ingrese nro: "))
			print(f"La division es igual a {division(nro1,nro2)}")
		except ZeroDivisionError:
				print("La division por cero es erronea")
		break
	if opcion == "5":
		break
	else: 
		print("opcion invalida")
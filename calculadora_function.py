#! /usr/bin/python
# -*- encoding: utf-8 -*-

# import sys
# sys.path.append('/Library/Python/2.7/site-packages')
# import colour

def calculadora(operacion, a, b):
	valor1 = a
	valor2 = b

	if operacion == "+":
		resultado = int(valor1) + int(valor2)
	elif operacion == "-":
		resultado = int(valor1) - int(valor2)
	elif operacion == "*":
		resultado = int(valor1) * int(valor2)
	elif operacion == "/":
		resultado = float(valor1) / float(valor2)
	return str(resultado)

def menu_calculadora():
	print "\033[1m" + "INGRESE LA OPERACION A REALIZAR: " + "\033[0m"
	print "Ingrese \033[31;1m+\033[0m para SUMA"
	print "Ingrese \033[32;1m-\033[0m para RESTA"
	print "Ingrese \033[33;1m*\033[0m para MULTIPLICACION"
	print "Ingrese \033[34;1m/\033[0m para DIVISION"
	print "Ingrese \033[35;1m%\033[0m para MODULO"
	data1 = raw_input()

	while True:
		data2 = raw_input("INGRESE EL PRIMER DATO: ")
		if len(data2) > 0 and data2.isdigit():
			break
		else:
			print "\033[93mLAME...! INGRESE SOLO CARACTERES NUMERICOS\033[0m"

	while True:
		data3 = raw_input("INGRESE EL SEGUNDO DATO: ")
		if len(data3) > 0 and data3.isdigit():
			break
		else:
			print "\033[93mLAME...! INGRESE SOLO CARACTERES NUMERICOS\033[0m"

	print ('El resultado de ' + '\033[36;1m' + str(data2) + '\033[0m' + ' ' + '\033[36;1m' +' '.join(str(data1) + str(data3)) + '\033[0m' + " es: " + calculadora(data1, data2, data3))
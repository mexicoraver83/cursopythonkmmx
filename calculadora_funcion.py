#! /usr/bin/python
# -*- encoding: utf-8 -*-

def calculadora(a, operacion, b):
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

data1 = raw_input("Ingrese el primer dato: ")
data2 = raw_input("Ingrese la operacion a realizar: ")
data3 = raw_input("Ingrese el segundo dato: ")

print ("El resultado de la operacion es:" + calculadora(data1, data2, data3))
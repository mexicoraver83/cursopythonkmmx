#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Author: jcastelo - 140418

def documento(edad):
	if edad  >= 18:
		print "Entregar IFE/INE"
	else:
		print "Es menor de edad"

def menu_consulta_edad():
	print "Ingrese \033[32;1msu edad \033[0m a analizar"
	data1 = int(raw_input())
	print ('El resultado del analisis para su edad es: '+ str(documento(data1)))

if __name__ == '__main__':
	menu_consulta_edad()
else:
	pass

# edad = input("Ingrese la edada a considerar: ")

# if edad >= 18:
# 	print "Entregar IFE/INE"
# else:
# 	print "Es menor de edad"
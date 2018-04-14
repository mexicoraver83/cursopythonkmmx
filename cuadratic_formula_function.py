#!/usr/bin/python
# -*- encoding: utf-8 -*-
import math

# Formula cuadratica

def cuadratica():

	# Obteniendo el coheficinete de los terminos

	a = float(input("Ingrese el \033[32;1mPRIMER\033[0m coheficiente \033[32;1ma\033[0m: " ))
	b = float(input("Ingrese el \033[33;1mSEGUNDO\033[0m coheficiente \033[33;1mb\033[0m: " ))
	c = float(input("Ingrese el \033[34;1mTERCER\033[0m coheficiente \033[34;1mc\033[0m: " ))

	Base = math.sqrt((b * b) - 4 * a * c) # Base
	positiva = (-b + Base) / (2 * a) # Solucion Positiva
	negativa = (-b - Base) / (2 * a) # Solucion Negativa

	print("Las soluciones son:", positiva, negativa )

if __name__ == '__main__':
	cuadratica()
else:
	pass
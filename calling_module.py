#! /usr/bin/python
# -*- encoding: utf-8 -*-
#Author: jcastelo - 140418

import cuadratic_formula_function
import calculadora_function

print "\033[1m" + "INGRESE LA OPERACION A REALIZAR: " + "\033[0m"
print "Ingrese \033[31;1m1\033[0m para CALCULAR LAS RAICES DE LA FORMULA CUADRATICA (\033[31;1maka la chicharronera\033[0m)"
print "Ingrese \033[32;1m2\033[0m para USAR SU CALCULADORA"

option = int(raw_input())
print "La opcion es: ", option

if option == 1:
	cuadratic_formula_function.cuadratica()
elif option == 2:
	calculadora_function.menu_calculadora()
else option == 3:
	ife_ine_function.documento()

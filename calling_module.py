#! /usr/bin/python
# -*- encoding: utf-8 -*-
#Author: jcastelo - 140418

import cuadratic_formula_function
import calculadora_function
import ife_ine_function

print "\033[1m" + "INGRESE LA OPERACION A REALIZAR: " + "\033[0m"
print "Ingrese \033[31;1m1\033[0m para CALCULAR LAS RAICES DE LA FORMULA CUADRATICA (\033[31;1maka la chicharronera\033[0m)"
print "Ingrese \033[32;1m2\033[0m para USAR SU CALCULADORA"
print "Ingrese \033[33;1m3\033[0m para CONSULTAR SI REQUIRE DOCUMENTO"

option = int(raw_input())
# print option

if option == 1:
	cuadratic_formula_function.cuadratica()
elif option == 2:
	calculadora_function.menu_calculadora()
elif option == 3:
	ife_ine_function.menu_consulta_edad()

#! /usr/bin/python
# -*- encoding: utf-8 -*-

# To do list:

# La segnda letra no puede ser vocal en el primer apellido
# No dejar al usuario que pase sin introducir su apellido

first_name = raw_input("Ingrese su primer nombre completo: ")
second_name = raw_input("Ingrese su segundo nombre completo: ")
first_ln = raw_input("Ingrese su primer apellido: ")
second_ln = raw_input("Ingrese su segundo apellido: ")
year = raw_input("Ingrese su anho de nacimiento: ")
mes = raw_input("Ingrese su mes de nacimiento: ")
dia = raw_input("Ingrese su dia de nacimiento: ")
homoclave = "xxx"

prohibit_list = ['PUTO', 'PENE', 'PUTA', 'BACA', 'VACA']

primer_termino = first_ln[ :2]
segundo_termino = second_ln[ :1]

if len(str(second_name)) == 0:
	tercer_termino = first_name[ :1]
	print "Test"
elif first_name == "jose" or first_name == "maria":
	tercer_termino = second_name[ :1]
else:
	tercer_termino = first_name[ :1]

if len(year) == 4:
	cuarto_termino = year[2: ]
else:
	cuarto_termino = year

if len(mes) == 1:
	quinto_termino = "0" + str(mes)
else:
	quinto_termino = mes
#print len(mes)

if len(dia) == 1:
	sexto_termino = "0" + str(dia)
else:
	sexto_termino = dia
#print len(dia)

# Evaluando lista prohibida

initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + str.upper(tercer_termino)
#print initial_evaluation

check = initial_evaluation in prohibit_list
#print check

if check == True:
	initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + 'X'
else:
	initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + str.upper(tercer_termino)


#RFC PRINT
print 'Tu RFC es: ' + initial_evaluation + str(cuarto_termino) + str(quinto_termino) + str(sexto_termino) + str.upper(homoclave)

###############################################################
# Check this later if you want to evalaute based  on indexing #
###############################################################

#if 0 <= prohibit_list.index(initial_evaluation) < len(initial_evaluation):
# 	print initial_evaluation
# else:
# 	print 'done'
#	initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + 'X'
#else:
#	initial_ev








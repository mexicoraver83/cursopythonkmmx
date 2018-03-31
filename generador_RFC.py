#! /usr/bin/python
# -*- encoding: utf-8 -*-

# Generador de RFC

# To do list:

# La segnda letra no puede ser vocal en el primer apellido


while True:
	first_name = raw_input("Ingrese su primer nombre completo: ")
	if len(first_name) > 0:
		if first_name.isalpha():
			break
		else:
			print("\033[93mLAME...! NO SE ACEPTAN CARACTERES NUMERICOS...INGRESE SOLO CARACTERES ALFABETICOS\033[0m")
while True:
	second_name = raw_input("Ingrese su segundo nombre completo (presione enter si no tiene): ")
	if second_name.isalpha():
		break
	else:
		print "\033[93mLAME...! NO SE ACEPTAN CARACTERES NUMERICOS...INGRESE SOLO CARACTERES ALFABETICOS\033[0m"

while True:
 	first_ln = raw_input("Ingrese su primer apellido: ")
 	if len(first_ln) > 0:
 		if first_ln.isalpha():
 			break
 		else:
 			print "\033[93mLAME...! NO SE ACEPTAN CARACTERES NUMERICOS...INGRESE SOLO CARACTERES ALFABETICOS\033[0m"

while True:
	second_ln = raw_input("Ingrese su segundo apellido: ")
	if len(second_ln) > 0:
		if second_ln.isalpha():
			break
		else:
			print "\033[93mLAME...! NO SE ACEPTAN CARACTERES NUMERICOS...INGRESE SOLO CARACTERES ALFABETICOS\033[0m"

while True:
	year = raw_input("Ingrese su anho de nacimiento: ")
	if len(year) > 0:
		if year.isdigit():
			break
		else:
			print "\033[93mLAME...! NO SE ACEPTAN CARACTERES ALFABETICOS...INGRESE SOLO CARACTERES NUMERICOS\033[0m"

while True:
	mes = raw_input("Ingrese su mes de nacimiento: ")
	if len(mes) > 0:
		if mes.isdigit():
			break
		else:
			print "\033[93mLAME...! NO SE ACEPTAN CARACTERES ALFABETICOS...INGRESE SOLO CARACTERES NUMERICOS\033[0m"

while True:
	dia = raw_input("Ingrese su dia de nacimiento: ")
	if len(dia) > 0:
		if dia.isdigit():
			break
		else:
			print "\033[93mLAME...! NO SE ACEPTAN CARACTERES ALFABETICOS...INGRESE SOLO CARACTERES NUMERICOS\033[0m"

homoclave = "xxx"

prohibit_list = ['BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA','CAGO', 'CAKA', 'CAKO', 'COGE', 'COJA', 'COJE', 'COJI', 'COJO', 'CULO', 'FETO', 'GUEY', 'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 'KOGE', 'COJO', 'KAKA', 'KULO', 'MAME', 'MAMO', 'MEAR', 'MEAS', 'MEON', 'MION', 'MOCO', 'MULA', 'PEDA','PEDO', 'PENE', 'PUTA', 'PUTO', 'QULO', 'RATA','RUIN']

# Primer termino

primer_termino = first_ln[ :2]

# Segundo termino

segundo_termino = second_ln[ :1]

# Tercer Termino
if len(str(second_name)) == 0:
	tercer_termino = first_name[ :1]
#	print "Test"
elif first_name == "jose" or first_name == "maria" or first_name == "Jose" or first_name == "Maria" or first_name == "JOSE" or first_name == "MARIA":
	tercer_termino = second_name[ :1]
else:
	tercer_termino = first_name[ :1]

# Cuarto terminno

if len(year) == 4:
	cuarto_termino = year[2: ]
else:
	cuarto_termino = year

# Quinto termino

if len(mes) == 1:
	quinto_termino = "0" + str(mes)
else:
	quinto_termino = mes

# Sexto termino

if len(dia) == 1:
	sexto_termino = "0" + str(dia)
else:
	sexto_termino = dia

# Here we are grouping first 3 terms to evaluate prohibit list
initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + str.upper(tercer_termino)

# Evaluando lista prohibida
check = initial_evaluation in prohibit_list

if check == True:
	initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + 'X'
else:
	initial_evaluation = str.upper(primer_termino) + str.upper(segundo_termino) + str.upper(tercer_termino)

#RFC PRINT
print '\033[94;4m' + 'Tu RFC es: ' + initial_evaluation + str(cuarto_termino) + str(quinto_termino) + str(sexto_termino) + str.upper(homoclave)

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








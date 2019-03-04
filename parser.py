from error import exit_message
from print_poly import print_poly
import sys

def get_degree(coeffs, expr):
	len_expr = len(expr)
	if len_expr == 1:
		coeffs['exposant'] = 1
		coeffs['coeff'] = 1 if coeffs['coeff'] == 0 else coeffs['coeff']
		return
	elif len_expr == 2 or expr[2] == '-':
		exit_message("Wrong syntax of power : ", expr)
	after_power = expr[2:]
	try:
		isfloat = float(after_power)
		isint = long(isfloat)
		if isint != isfloat:
			coeffs['exposant'] = isfloat
		else:
			coeffs['exposant'] = isint
		return
	except:
		exit_message("Wrong syntax of power : ", expr)

def check_symbol(exploded, i, neg, equal):
	if exploded[i] == "-":
		neg = 1
	if exploded[i] == "=" and equal == 0:
		equal = 1
	elif exploded[i] == "=":
		exit_message("There must be only one '=' character")
	i += 1
	if exploded[i] == "+" or exploded[i] == "-" or exploded[i] == "=":
		exit_message("Wrong syntax : ", exploded[i])
	return i,neg, equal

def handle_multiplication(array, i, coeff, length):
	if i == length or i + 1 == length or array[i + 1] == "=":
		return i
	i += 1
	if array[i] == "*":
		i += 1
	elif array[i] == "+" or array[i] == "-" or array[i] == "=":
		return i - 1
	if array[i][0] == 'X':
		get_degree(coeff, array[i])
		return i
	else:
		exit_message("Wrong syntax after : ", array[i])

def parser(polynome, expr):
	i = 0
	equal = 0
	exploded = expr[0].split()
	length = len(exploded)
	while i < length:
		neg = 0
		coeffs = {'exposant': 0, 'coeff': 0}
		if i != 0 and i != length - 1 and \
			(exploded[i] == "+" or exploded[i] == "-" or exploded[i] == "="):
			i,neg, equal = check_symbol(exploded, i, neg, equal)
		if exploded[i][0] == "X":
			coeffs['coeff'] = 1;
			get_degree(coeffs, exploded[i])
			if neg == 1:
				coeffs['coeff'] *= -1
			if equal == 1:
				coeffs['coeff'] *= -1
		else:
			try:
				isfloat = float(exploded[i])
				if round(isfloat, 0) != isfloat:
					coeffs['coeff'] = isfloat
				else:
					isint = long(isfloat)
					coeffs['coeff'] = isint
				if neg == 1:
					coeffs['coeff'] *= -1
				if equal == 1:
					coeffs['coeff'] *= -1
				i = handle_multiplication(exploded, i, coeffs, length)
			except ValueError:
				exit_message("Wrong character in the expression : ", exploded[i])
		if coeffs['coeff'] != 0:
			polynome.append(coeffs)
		i += 1
	if equal == 0:
		exit_message("There is no equal character in the expression")

def check_invalid_exponent(poly):
	for elmt in poly:
		if elmt['exposant'] > 2:
			exit_message("The polynomial degree is stricly greater than 2, I can't solve.")
		if elmt['exposant'] != 0 and elmt['exposant'] != 1 and elmt['exposant'] != 2:
			exit_message("Cannot resolve polynoms with exponent : " + str(elmt['exposant']))


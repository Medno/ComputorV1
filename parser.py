from error import exit_message

def get_degree(coeffs, expr):
	len_expr = len(expr)
	if len_expr == 1:
		coeffs['exposant'] = 1
		coeffs['coeff'] = 1 if coeffs['coeff'] == 0 else coeffs['coeff']
		return
	elif len_expr == 2:
		exit_message("Wrong syntax of power : ", expr)
	after_power = expr[2:]
	try:
		degree = float(after_power)
		coeffs['exposant'] = degree
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
		return i
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
		else:
			try:
				isfloat = float(exploded[i])
				isint = int(exploded[i])
				if isint != isfloat:
					coeffs['coeff'] = isfloat
				else:
					coeffs['coeff'] = isint
				if neg == 1:
					coeffs['coeff'] *= -1
				if equal == 1:
					coeffs['coeff'] *= -1
				i = handle_multiplication(exploded, i, coeffs, length)
			except:
				exit_message("Wrong character in the expression : ", exploded[i])
		polynome.append(coeffs)
		i += 1
	if equal == 0:
		exit_message("There is no equal character in the expression")


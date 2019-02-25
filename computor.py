import sys
from sqrt import *

"""
	Organisation:

OK	-> Recode sqrt function

OK	-> Get the polynomial
		-> Split ?

	-> Check valid characters (all digits, get an alpha and let's say that's the variable ?)
	
	-> Put all factors on the left
		-> Print it
	
	-> Categorization of degrees
		-> Structure like [[exp, coeff], ...]
			Example: " 4 + 2 * X + X^2 = 2 - X "
			-> [ [0, 4], [1, 2], [2, 1], [0, -2], [1, 1] ]
		-> Refacto all degrees
	
	-> Compute the discriminant

	-> If the discriminant = 0
		-> 
"""

def handle_degrees(coeffs, i, array):
	length = len(array)
	if length <= i + 1 or (array[i + 1] and array[i + 1] != "^"):
		if array[i + 1] == "+" or array[i + 1] == "-" or array[i + 1] == "=":
			coeffs[1] = 1
			return
		print("Wrong syntax after : ", array[i])
		sys.exit(1)
	if length <= i + 2:
		print("Wrong syntax after : ", array[i + 1])
		sys.exit(1)
	try:
		coeffs[1] = float(array[i + 2])
	except:
		print("Wrong character in the expression : ", array[i])
		sys.exit(1)

def parser(polynome, expr):
	i = 0
	exploded = expr[0].split()
	length = len(exploded)
	while i < length:
		neg = 0
		coeffs = [0.0, 0.0]
		print(i)
		if exploded[i] == "+" or exploded[i] == "-" or exploded[i] == "=":
			if exploded[i] == "-":
				neg = 1
			i += 1
		if exploded[i] == "X":
			handle_degrees(coeffs, i, exploded)
			i += 1
		else:
			try:
				coeffs[0] = float(exploded[i])
				if neg == 1:
					coeffs[0] *= -1
				i += 1
				if i < length and exploded[i] == "X":
					handle_degrees(coeffs, i, exploded)
			except:
				print("Wrong character in the expression : ", exploded[i])
				sys.exit(1)
		polynome.append(coeffs)
		print(polynome)
		i += 1

def main():
	polynome = list()
	expression = sys.argv[1:]
	if len(expression) != 1:
		print("Wrong number of parameters")
		sys.exit(1)
	parser(polynome, expression)

main()

import sys
from parser import parser, check_invalid_exponent
from error import exit_message
from print_poly import *
from refacto import refacto
from resolver import resolve_polynome

"""
	Organisation:

OK	-> Recode sqrt function

OK	-> Get the polynomial
		-> Split ?

OK	-> Check valid characters (all digits, get an alpha and let's say that's the variable ?)
	
OK	-> Put all factors on the left
OK		-> Print it
	
	-> Categorization of degrees
		-> Structure like [[exp, coeff], ...]
			Example: " 4 + 2 * X + X^2 = 2 - X "
			-> [ [0, 4], [1, 2], [2, 1], [0, -2], [1, 1] ]
		-> Refacto all degrees
	
	-> Compute the discriminant

	-> If the discriminant = 0
		-> 
"""

def computor():
	polynome = list()
	expression = sys.argv[1:]
	if len(expression) != 1:
		exit_message("Wrong number of parameters")
	parser(polynome, expression)
	polynome = refacto(polynome)
	print_refacto(polynome)
	check_invalid_exponent(polynome)
	resolve_polynome(polynome)

computor()

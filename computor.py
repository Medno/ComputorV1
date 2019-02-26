import sys
from sqrt import *
from parser import parser
from error import exit_message
from print_poly import print_polynome

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

def computor():
	polynome = list()
	expression = sys.argv[1:]
	if len(expression) != 1:
		exit_message("Wrong number of parameters")
	parser(polynome, expression)
	print(polynome)
	print_polynome(polynome)

computor()

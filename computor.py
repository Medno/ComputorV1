import sys
from parser import parser, check_invalid_exponent
from error import exit_message
from print_poly import *
from refacto import refacto
from resolver import resolve_polynome

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

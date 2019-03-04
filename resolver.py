# coding: utf8
from ft_maths import sqrt, pgcd
from refacto import refacto_sqrt
from print_solutions import print_unfactored_solution, print_factored_solution

def resolve_first_degree(poly):
	z_degree = poly[0] if poly[0]['exposant'] == 0 else {'coeff': 0,'exposant': 0}
	f_degree = poly[0] if poly[0]['exposant'] == 1 else poly[1]
	gcd = pgcd(float(z_degree['coeff']), float(f_degree['coeff']))
	gcd = long(gcd) if long(gcd) == float(gcd) else 1
	result = -1 * float(z_degree['coeff']) / float(f_degree['coeff'])
	print("The solution is :")
	if float(result) == long(result):
		print(long(result))
	else:
		print(result)
		print("That can be written as: " + str((-1 * z_degree['coeff']) / gcd) +\
		" / " + str(f_degree['coeff'] / gcd))

def resolve_second_degree(poly):
	z_degree = next((elmt for elmt in poly if elmt['exposant'] == 0), {'coeff': 0, 'exposant': 0})
	f_degree = next((elmt for elmt in poly if elmt['exposant'] == 1), {'coeff': 0, 'exposant': 1})
	s_degree = poly[-1]
	a = s_degree['coeff']
	b = f_degree['coeff']
	c = z_degree['coeff']
	discriminant = pow(b, 2) - (4 * a * c)
	print("Computation of the discriminant: \
	\nΔ = " + str(b) + "^2 - (4 * " + str(a) + " * " + str(c) + ") = " + str(pow(b, 2))\
	+ " - (" + str(4 * a * c)) + ")"
	print("Discriminant : " + str(discriminant))
	sqrt_dis = sqrt(abs(discriminant))
	if discriminant == 0:
		print("Discriminant is nil, the unique solution is:")
		result = -1.0 * b / (2.0 * a)
		if float(result) == long(result):
			print(int(result))
		else:
			print(result)
			print("That can be written as: " + str(-1 * b) + " / " + str(2 * a))
	elif discriminant > 0:
		print("Discriminant is strictly positive, the two solutions are:")
		x1 = (-1.0 * b + sqrt_dis) / (2 * a)
		x2 = (-1.0 * b - sqrt_dis) / (2 * a)
		div, root = refacto_sqrt(discriminant)
		gcd = reduce(lambda x, y: pgcd(x, y), [-1.0 * b, div, 2 * a]) if div > 1 else 1
		print_unfactored_solution(a, b, abs(discriminant), 1)
		if float(x1) == long(x1):
			print(long(x1))
		else:
			if discriminant != root:
				print_factored_solution(a, b, div, root, gcd, 1, 0)
			print(x1)

		print_unfactored_solution(a, b, abs(discriminant), 0)
		if float(x2) == long(x2):
			print(long(x2))
		else:
			if discriminant != root:
				print_factored_solution(a, b, div, root, gcd, 0, 0)
			print(x2)
	else:
		abs_disc = abs(discriminant)
		print("Discriminant is strictly negative, the two solutions are:")
		x1 = complex(-1 * b, sqrt_dis) / (2 * a)
		x2 = complex(-1 * b, -1 * sqrt_dis) / (2 * a)
		div, root = refacto_sqrt(abs_disc)
		gcd = reduce(lambda x, y: pgcd(x, y), [-1.0 * b, div, 2 * a]) if div > 1 else 1
		print_unfactored_solution(a, b, abs_disc, 1, 1)
		if abs_disc != root:
			print_factored_solution(a, b, div, root, gcd, 1, 1)
		print(x1)
		print_unfactored_solution(a, b, abs_disc, 0, 1)
		if abs_disc != root:
			print_factored_solution(a, b, div, root, gcd, 0, 1)
		print(x2)
		
def resolve_polynome(polynome):
	if len(polynome) == 0:
		print("All real numbers are solutions")
	elif polynome[-1]['exposant'] == 0:
		print("There is no solution")
	elif polynome[-1]['exposant'] == 1:
		resolve_first_degree(polynome)
	else:
		resolve_second_degree(polynome)
	

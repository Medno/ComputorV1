from ft_maths import sqrt, pgcd
from refacto import refacto_sqrt

def resolve_first_degree(poly):
	zero_degree = poly[0] if poly[0]['exposant'] == 0 else {'coeff': 0,'exposant': 0}
	result = -1 * float(zero_degree['coeff']) / float(poly[1]['coeff'])
	print("The solution is :")
	if float(result) == int(result):
		print(int(result))
	else:
		print(result)
		print("That can be written as: " + str(-1 * zero_degree['coeff']) + " / " + str(poly[1]['coeff']))

def resolve_second_degree(poly):
	z_degree = next((elmt for elmt in poly if elmt['exposant'] == 0), {'coeff': 0, 'exposant': 0})
	f_degree = next((elmt for elmt in poly if elmt['exposant'] == 1), {'coeff': 0, 'exposant': 1})
	s_degree = poly[-1]
	a = s_degree['coeff']
	b = f_degree['coeff']
	c = z_degree['coeff']
	discriminant = pow(b, 2) - (4 * a * c)
	print("Discriminant : " + str(discriminant))
	sqrt_dis = sqrt(abs(discriminant))
	if discriminant == 0:
		print("Discriminant is nil, the unique solution is:")
		result = -1.0 * b / (2.0 * a)
		if float(result) == int(result):
			print(int(result))
		else:
			print(result)
			print("That can be written as: " + str(-1 * b) + " / " + str(2 * a))
	elif discriminant > 0:
		print("Discriminant is strictly positive, the two solutions are:")
		x1 = (-1.0 * b + sqrt(discriminant)) / (2 * a)
		x2 = (-1.0 * b - sqrt(discriminant)) / (2 * a)
		if float(x1) == int(x1):
			print(int(x1))
		else:
			print(x1)
		if float(x2) == int(x2):
			print(int(x2))
		else:
			print(x2)
		div, root = refacto_sqrt(discriminant)
		gcd_1 = reduce(lambda x, y: pgcd(x, y), [-1.0 * b, div, 2 * a]) if div > 1 else 1
		gcd_2 = reduce(lambda x, y: pgcd(x, y), [-1.0 * b, - 1 * div, 2 * a]) if div > 1 else 1
		if int(x1) != float(x1):
			if int(gcd_1) != float(gcd_1):
				gcd_1 = 1
			else:
				gcd_1 = int(gcd_1)
			is_fract = 2 * a / gcd_1 > 1
			print("That can be written as: " + ("(" if is_fract else "") +\
			str(-1 * b / gcd_1) + " + " + \
			(str(div / gcd_1) + " * " if div / gcd_1 != 1 else "") + \
			"sqrt(" + str(root) + ")" + (")" if is_fract else "") + \
			(" / " + str(2 * a / gcd_1) if is_fract else ""))
		if int(x2) != float(x2):
			if int(gcd_2) != float(gcd_2):
				gcd_2 = 1
			else:
				gcd_2 = int(gcd_2)
			is_fract = 2 * a / gcd_2 > 1
			print("That can be written as: " + ("(" if is_fract else "") +\
			str(-1 * b / gcd_2) + " - " + \
			(str(div / gcd_2) + " * " if div / gcd_2 != 1 else "") + \
			"sqrt(" + str(root) + ")" + (")" if is_fract else "") + \
			(" / " + str(2 * a / gcd_2) if is_fract else ""))

	else:
		print("Discriminant is strictly negative, the two solutions are:")
		x1 = complex(-1 * b, sqrt_dis) / (2 * a)
		x2 = complex(-1 * b, -1 * sqrt_dis) / (2 * a)
		print(x1)
		print(x2)
		
def resolve_polynome(polynome):
	if len(polynome) == 0:
		print("Every real number is a solution")
	elif polynome[-1]['exposant'] == 0:
		print("There is no solution")
	elif polynome[-1]['exposant'] == 1:
		resolve_first_degree(polynome)
	else:
		resolve_second_degree(polynome)
	

def print_poly(poly):
	res = ""
	length = len(poly)
	if length == 0:
		res += "0 "
	for elmt in poly:
		if elmt['coeff'] < 0:
			res += "- "
		elif elmt != poly[0]:
			res += "+ "
		if elmt['exposant'] != 0 and abs(elmt['coeff']) != 1:
			res += str(abs(elmt['coeff'])) + " * "
		if elmt['exposant'] == 0:
			res += str(abs(elmt['coeff']))
		if elmt['exposant'] != 0:
			res += "X"
		if elmt['exposant'] > 1:
			res += "^" + str(elmt['exposant'])
		res += " "
	res += "= 0"
	return res

def print_refacto(poly):
	print("Reduced form: " + print_poly(poly))
	degree = "0" if len(poly) == 0 else str(poly[-1]['exposant'])
	print("Polynomial degree: " + degree)

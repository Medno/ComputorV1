def print_polynome(polynome):
	res = ""
	length = len(polynome)
	for element in polynome:
		if element != polynome[0] and element != polynome[length - 1]:
			res += "+ " if element['coeff'] >= 0 else "- "
		if element['coeff'] > 1 or element['coeff'] < -1 or \
			(element['coeff'] == 1 and element['exposant'] == 0):
			if element['coeff'] < 0:
				res += "- " + str(-1 * element['coeff']) + " "
			else:
				res += str(element['coeff'])
			if element['coeff'] > 1 and element['exposant'] > 0:
				res += " * "
		if element['exposant'] != 0:
			res += "X"
			if element['exposant'] > 1:
				res += "^"
				res += str(int(element['exposant']))

		if element != polynome[length - 1]:
			res += " "
	res += "= 0"
	print(res)


from ft_maths import pgcd, sqrt

def refacto(poly):
	sorted_poly = sorted(poly, key=lambda k: k['exposant'])
	new_poly = []
	coeff = {}
	for i, elmt in enumerate(sorted_poly):
		if i != 0 and elmt['exposant'] != coeff['exposant']:
			new_poly.append(coeff)
			coeff = elmt
		elif i == 0:
			coeff = elmt
		else:
			coeff['coeff'] += elmt['coeff']
	new_poly.append(coeff)
	poly = [elmt for elmt in new_poly if elmt['coeff'] != 0]
	if len(poly) > 0 and poly[-1]['exposant'] != 0:
		values = map(lambda x: x['coeff'], poly)
		gcd = reduce(lambda x,y: pgcd(x, y), values)
		if gcd > 1:
			for elmt in poly:
				elmt['coeff'] /= gcd
	return poly

def refacto_sqrt(disc):
	if disc <= 2:
		return 1, disc
	i = 2.0
	while i < disc / 2:
		div = disc / i
		tmp = sqrt(div)
		if int(tmp) == float(tmp):
			return int(tmp), int(i)
		i += 1
	return 1, disc

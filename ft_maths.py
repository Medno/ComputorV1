def sqrt(n):
	x = float(n / 4)
	e = (n - (x * x)) / 2 * x
	while x != e:
		e = x
		x = (x + (n / x)) / 2
	return x

def pgcd(x, y):
	while y:
		x, y = y, x % y
	return x

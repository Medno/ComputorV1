def print_unfactored_solution(a, b, disc, first, comp = 0):
	print("The " + ("first" if first else "second") + " solution is: " + \
	"(" + str(-1 * b) + (" + " if first else " - ") + \
	("j * " if comp else "") + "sqrt(" + str(disc) + ")) / " + str(2 * a))

def print_refactored_sqrt(a, b, div, root, gcd, first, comp, is_fract):
	print("That can be written as: " + ("(" if is_fract else "") +\
	(str((-1 * b) / gcd) + (" + " if first else " - ") if b != 0 else "") + \
	(str(div / gcd) + " * " if div / gcd != 1 else "") + ("j * " if comp else "") + \
	"sqrt(" + str(root) + ")" + (")" if is_fract else "") + \
	(" / " + str(2 * a / gcd) if is_fract else ""))

def print_factored_solution(a, b, div, root, gcd, first, comp):
	print_refactored_sqrt(a, b, div, root, 1, first, comp, 1)
	if long(gcd) != float(gcd):
		gcd = 1
	else:
		gcd = int(gcd)
	if gcd != 1:
		print_refactored_sqrt(a, b, div, root, gcd, first, comp, 0)

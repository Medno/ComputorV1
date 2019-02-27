import os

polynomes = [ \
	"X - X = 3",
	"X - X = 0",
	"1 + 2 + 3 = 4",
	"X + 1 = 0",
	"X = 3",
	"1 * X = 3",
	"1 * X  + 2 * X^1 + X - X = 3",
	"X^2 + 2 - X^1 = 3",
	"X^2 + 2 - 2 * X^1 = 3",
	"X^2 + 2 = 0",
	"2 * X^1 + X^2 = 0",
	"X^2 + 2 + 3 * X^1 = 3",
	"X^2 + 2 * X^1 = -1",
	"4 * X^2 + 2 * X^1 = -2",
	"5 + 4 * X + X^2 = X^2",
	"Error",
	"X^-2 + 2 + 3 * X^1 = 3",
	"+ X^2 + 2 + 3 * X^1 = 3",
	"X^2 + 2 + 3 * X^1 ",
	"X^2 + 2 + 3 ** X^1 = 0",
	"X^^2 + 2 + 3 * X^1 = 0",
	"Y^^2 + 2 + 3 * X^1 = 0",
	"X^2 + + 2 + 3 * X^1 = 3",
	"X^3 + 2 + 3 * X^1 = 3",
	"X^1.2 + 2 + 3 * X^1 = 3",
	]

for example in polynomes:
	print("Original : -> " + example)
	os.system("python computor.py \"" + example + "\"")
	print("")

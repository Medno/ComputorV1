import os

polynomes = [ \
	"X + 1 = 0",
	"X^2 + 2 = 0",
	"2 * X^1 + X^2 = 0",
	"X^2 + 2 + 3 * X^1 = 3",
	"1 + 2 + 3 = 4"
	]

for example in polynomes:
	print(example)
	os.system("python computor.py \"" + example + "\"")

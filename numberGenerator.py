from random import randint, choice

letters = "ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
letters = [letter for letter in letters]

def generateNumber():
	number = ''

	number += choice(letters)

	for _ in range(3):
		number += str(randint(0, 9))

	number += choice(letters)
	number += choice(letters)

	for _ in range(2):
		number += str(randint(0, 9))

	return number


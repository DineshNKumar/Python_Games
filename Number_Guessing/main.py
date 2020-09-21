import random


def game():
	guesses = []

	my_computer = random.randint(1,70)

	player_input = int(input('Enter a number between 1 - 70 : '))
	guesses.append(player_input)

	while player_input != my_computer:
		if player_input > my_computer:
			print('Number is too high')
		else:
			print('Number is too low')
		player_input = int(input('Enter a number between 1 - 70 : '))
		guesses.append(player_input)
	else:
		print('Good job')
		print('You took %i guesses' % len(guesses))
		print('These were your guesses ', guesses)


if __name__ == '__main__':
	game()


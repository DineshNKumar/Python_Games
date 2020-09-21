import random 

lottery_number = []

for i in range(0, 6):
	number = random.randint(100000, 50000000)
	while number in lottery_number:
		number = random.randint(100000, 50000000)

	lottery_number.append(number)

lottery_number.sort()
print(lottery_number)
lottery_number.clear()
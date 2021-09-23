from random import randint

# Asking what kind of dice they want to roll and the amount

dice = input("What kind of dice do you want to trow? (how many sides)\n")
amount = input (f"How many of the d{dice} do you want to trow?\n")

# calculating the score of the dice and returning the total
value_total = 0 
for i in range(int(amount)):
	value = randint(0, int(dice))
	value_total += value
	
print(value_total)

from random import randint

# Asking what kind of dice they want to roll and the amount
dice = input("What kind of dice do you want to throw? (how many sides)\n")
amount = input (f"How many of the d{dice} do you want to throw?\n")

# calculating the score of the dice and returning the total
value_total = 0 
value_list = []
for i in range(int(amount)):
	value = randint(0, int(dice))
	value_list.append(value)
	value_total += value

#printing the values	
print(f"The value of the thrown dice are: { {*value_list} }\nWhich brings the total to {value_total}")

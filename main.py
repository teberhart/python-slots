import random

MAX_LINES = 3

SLOTS_LINES = MAX_LINES
SLOTS_COLUMNS = 3

symbols_count = {
	"J": 2,
	"Q": 4,
	"K": 6,
	"A": 8
}

# Function used to "spin" the slot machine
def get_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, count in symbols.items():
		for _ in range(count):
			all_symbols.append(symbol)

	columns = []
	for _ in range(cols):
		column = []
		column_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(column_symbols)
			column_symbols.remove(value)
			column.append(value)

		columns.append(column)

	return columns

# Function used to print the spin in a readable manner
def print_slots(columns):
	lines = []
	for row in range(len(columns[0])):
		line = ""
		for i, column in enumerate(columns):
			if i != (len(columns) - 1):
				line += column[row] + "|"
			else:
				line += column[row]
		lines.append(line)
		print(line)

	return lines

# Function used to get the amount deposited by the user
def deposit():
	while True:
		amount = input("What amount would you like to deposit into your balance ? ")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				break
			else:
				print("The amount must be greater than 0.")
		else:
			print("The amount must deposited must be an integer, greater than 0.")

	return amount

# Function used to get the amount of lines the user wants to bet on
def amount_of_lines():
	while True:
		number = input("How many lines would you like to bet on ? (1-" + str(MAX_LINES) + ") ")
		if number.isdigit():
			number = int(number)
			if 1 <= number <= MAX_LINES:
				break
			else :
				print("You can only bet on 1 to " + str(MAX_LINES) + " lines, player.")
		else:
			print("Please enter a number of lines to bet on.")

	return number

# Function used to get the amount of points the user wants to bet per line
def amount_betted(balance, lines):
	while True:
		amount = input("What amount would you like to bet on each line this time ? ")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				print(f"You're trying to bet {amount*lines} ? Let me check ...")
				if (amount * lines) < balance:
					print("This is all good !")
					break
				else :
					print("The amount you bet can't be greater than your balance.")
			else:
				print("The amount must be greater than 0.")
		else:
			print("The amount better must be an integer, greater than 0.")

	return amount

# Function used to get the amount betted by the user
def bet(balance):
	lines = amount_of_lines()
	bet = amount_betted(balance, lines)
	total = lines * bet

	print(f"You are betting {bet} on {lines} lines. Total bet is {total}.")

def main():
	balance = deposit()
	print("Your balance is " + str(balance))
	bet(balance)

	spin = get_spin(SLOTS_LINES, SLOTS_COLUMNS, symbols_count)
	print_slots(spin)

main()
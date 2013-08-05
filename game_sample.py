turn = "X"
map = [ [" ", " ", " "],
		[" ", " ", " "],
		[" ", " ", " "]]
done = False

# Functions:
def print_board():
	for i in range(0,3):
		for j in range(0,3):
			if j != 2:
				print(map[2-i][j] + "|"),
			else:
				print(map[2-i][j]),
		print("")

def check_done():
	for i in range(0,3):
		if map[i][0] == map[i][1] == map[i][2] != " " \
		or map[0][i] == map[1][i] == map[2][i] != " ":
			print(turn, "won!!!")
			return True

	if map[0][0] == map[1][1] == map[2][2] != " " \
	or map[0][2] == map[1][1] == map[2][0] != " ":
		print(turn, "won!!!")
		return True

	if " " not in map[0] and " " not in map[1] and " " not in map[2]:
		print("Draw")
		return True

	return False


# Main Program:

while done != True:
	print_board()

	print(turn, " 's turn")
	print()

	moved = False
	while moved != True:
		print ("Please select position by typing in a number:")
		print ("7|8|9")
		print ("4|5|6")
		print ("1|2|3")
		print()

		try:
			pos = input("Select: ")
			pos = int(pos)
			if pos <= 9 and pos >= 1:
				Y = pos/3
				X = pos%3
				if X != 0:
					X -= 1
				else:
					X = 2
					Y -= 1

				if map[Y][X] == " ":
					map[Y][X] = turn
					moved = True
					done = check_done()

					if done == False:
						if turn == "X":
							turn = "O"
						else:
							turn = "X"
		except:
			print("You need to add a numeric value")
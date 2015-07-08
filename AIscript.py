import aiprog

r1 = [0,0,0]
r2 = [0,0,0]
r3 = [0,0,0]

board = [r1,r2,r3]

# PRINTING BOARD & TURNS

def printBoard(board):
	print "\n"
	for i in board:
		for n in i:
			print n,
		print "\n"

def Pturn(n,board):
	
	print "Player " + str(n) + " :"
	prow = check123(raw_input("Which row? (1/2/3) \n >  ")) -1
	while (prow +1) <= 0 or (prow+1) > 3:
		print "Please re-enter row:"
		prow = check123(raw_input("Which row? (1/2/3) \n >  ")) -1

	pcol = check123(raw_input("Which col? (1/2/3) \n >  ")) -1
	while (pcol+1) <= 0 or (pcol+1) > 3:
		print "Please re-enter col:"
		pcol = check123(raw_input("Which col? (1/2/3) \n >  ")) -1

	if board[prow][pcol] == 0:
		board[prow][pcol] = n
		printBoard(board)
#		return rowCrit()
	else:
		printBoard(board)
		print "Sorry, it's taken. Try again!"
		Pturn(n,board)
#		return False

# def P2turn():
# 	print "Player 2 :"
# 	p2row = int(raw_input("Which row? (1/2/3) \n >  ")) -1
# 	p2col = int(raw_input("Which col? (1/2/3) \n >  ")) -1

# 	if board[p2row][p2col] == 0:
# 		board[p2row][p2col] = 2
# 		printBoard()
# 	else:
# 		printBoard()
# 		print "Sorry, it's taken. Try again!"
# 		P2turn()

# GAME OVER CRITERIA
def endCrit(board):
	for i in board:
		for n in i:
			if n == 0:
				return False
				break
	else:
		return True

def nrowmatch(nrow):
	x = 0
	y = 1
	for v in nrow:
		y = y*v
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

#def nrowmatch(nrow):
#	for i in range(len(nrow) - 1):
#		if nrow[i] == 0 or nrow[i] != nrow[i+1]:
#			return False
#	return True 


def rowCrit(board):
	for v in board:
		if nrowmatch(v):
			return True
			break
	else: 
		return False

def ncolmatch(ncol,board):
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][ncol]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def colCrit(board):
	for ncol in range(len(board[0])):
		if ncolmatch(ncol,board):
			return True
			break
	else: 
		return False

def leftdiagCrit(board):
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][i]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def rightdiagCrit(board):
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][2-i]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def winCrit(board):
	return rightdiagCrit(board) or leftdiagCrit(board) or colCrit(board) or rowCrit(board)

#GAME RUNS

def clearboard(board):
	r1 = [0,0,0]
	r2 = [0,0,0]
	r3 = [0,0,0]
	board = [r1,r2,r3]
	return board

def checkyn(inputt):
	if inputt == "y" or inputt == "n":
		return inputt
	else:
		inputt2 = str(raw_input("Please enter 'y' or 'n'.\n > ")).lower()
		return checkyn(inputt2)

def check123(inputt):
	if inputt == "1" or inputt == "2" or inputt == "3":
		return int(inputt)
	else:
		inputt2 = raw_input("Please enter '1' or '2' or '3'.\n > ")
		return check123(inputt2)

def replay(board):
	inputt = str(raw_input("Do you want to play again? (y/n) \n > ")).lower()
	answer = checkyn(inputt)
	if answer == "y":
		start_game(clearboard(board))
	else:
		print "Thanks for playing! \n ---------- Credits: Shannon Chan ----------"
		return True

def start_game(board):
	printBoard(board)
	inputt = raw_input("Do you want to begin first? (y/n)")
	who_starts = checkyn(inputt)
	if who_starts == "y":
		while not winCrit(board):
			Pturn(1,board)
			if winCrit(board):
				print "GAME OVER!!! You win!"
				if replay(board):
					return
			elif endCrit(board):
				print "GAME OVER!!! It's a draw!"
				if replay(board):
					return
			else:	
				ai = aiprog.AIprog(2,board)
				board[ai[0]][ai[1]] = 2
				print "AI played row %s , col %s" %((ai[0]+1),(ai[1]+1))
				printBoard(board)
				if endCrit(board):
					print "GAME OVER!!! It's a draw!"
					if replay(board):
						return
		else:
			print "GAME OVER!!! AI wins"
			if replay(board):
					return

	if who_starts == "n":
		while not winCrit(board):
			ai = aiprog.AIprog(1,board)
			board[ai[0]][ai[1]] = 1
			print "AI played row %s , col %s" %((ai[0]+1),(ai[1]+1))
			printBoard(board)
			if winCrit(board):
				print "GAME OVER!!! AI wins"
				if replay(board):
					return           # Bug: Break here but while - else statement still runs?
			elif endCrit(board):
				print "GAME OVER!!! It's a draw!"
				if replay(board):
					return
			else:
				Pturn(2,board)
				if endCrit(board):
					print "GAME OVER!!! It's a draw!"
					if replay(board):
						return
		else:
			print "GAME OVER!!! You win!"    # Runs despite break
			if replay(board):
					return

start_game(board)
#win = ""
#while True:
#	if P1turn():
#		win = "p1"
#		break
#	if P2turn():
#		win = "p2"
#		break
#print "GAME OVER!!! " + win + " wins"

#SOME CHANGE SOMEWHERE
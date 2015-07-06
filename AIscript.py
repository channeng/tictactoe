import aiprog

r1 = [0,0,0]
r2 = [0,0,0]
r3 = [0,0,0]

board = [r1,r2,r3]

# PRINTING BOARD & TURNS

def printBoard():
	print "\n"
	for i in board:
		for n in i:
			print n,
		print "\n"

def Pturn(n):
	
	print "Player " + str(n) + " :"
	
	prow = int(raw_input("Which row? (1/2/3) \n >  ")) -1
	while (prow +1) <= 0 or (prow+1) > 3:
		print "Please re-enter row:"
		prow = int(raw_input("Which row? (1/2/3) \n >  ")) -1

	pcol = int(raw_input("Which col? (1/2/3) \n >  ")) -1
	while (pcol+1) <= 0 or (pcol+1) > 3:
		print "Please re-enter col:"
		pcol = int(raw_input("Which col? (1/2/3) \n >  ")) -1

	if board[prow][pcol] == 0:
		board[prow][pcol] = n
		printBoard()
#		return rowCrit()
	else:
		printBoard()
		print "Sorry, it's taken. Try again!"
		Pturn(n)
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
def endCrit():
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


def rowCrit():
	for v in board:
		if nrowmatch(v):
			return True
			break
	else: 
		return False

def ncolmatch(ncol):
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][ncol]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def colCrit():
	for ncol in range(len(board[0])):
		if ncolmatch(ncol):
			return True
			break
	else: 
		return False

def leftdiagCrit():
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][i]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def rightdiagCrit():
	x = 0
	y = 1
	for i in range(3):
		y = y*board[i][2-i]
	x = x+y
	if x == 1 or x == 8:
		return True
	else:
		return False

def winCrit():
	return rightdiagCrit() or leftdiagCrit() or colCrit() or rowCrit()

#GAME RUNS
def start_game():
	printBoard()
	who_starts = raw_input("Do you want to begin first? (y/n)")
	if who_starts == "y":
		while not winCrit():
			Pturn(1)
			if winCrit():
				print "GAME OVER!!! You win!"
				break
			elif endCrit():
				print "GAME OVER!!! No one wins..."
				break
			ai = aiprog.AIprog(2,board)
			board[ai[0]][ai[1]] = 2
			printBoard()
			print "AI played row %s , col %s" %(ai[0],ai[1])
			if endCrit():
				print "GAME OVER!!! It's a draw..."
				break
		else:
			print "GAME OVER!!! AI wins"

	if who_starts == "n":
		while not winCrit():
			ai = aiprog.AIprog(1,board)
			board[ai[0]][ai[1]] = 1
			printBoard()
			print "AI played row %s , col %s" %(ai[0],ai[1])
			if winCrit():
				print "GAME OVER!!! AI wins"
				break
			elif endCrit():
				print "GAME OVER!!! No one wins..."
				break
			Pturn(2)
			if endCrit():
				print "GAME OVER!!! It's a draw..."
				break
		else:
			print "GAME OVER!!! You win!"

start_game()
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
import copy

#AI PROGRAM
r1 = [1,0,0]
r2 = [0,2,0]
r3 = [0,0,0]

board = [r1,r2,r3]

#DEFINE ROW WEIGHTAGES
def sumrow(playerX,row):
	i = 0
	for v in row:
		if v == playerX:
			i +=1
	return i

def searchopprow(playerX,row):
	if playerX == 1:
		i = 0
		for v in row:
			if v == 2:
				i +=1
		return i
	if playerX == 2:
		i = 0
		for v in row:
			if v == 1:
				i +=1
		return i

def fchckrow(playerX,row):
	if searchopprow(playerX,row)>0:
		return 0
	else:
		if sumrow(playerX,row) ==2:
			return 3
		else: 
			return sumrow(playerX,row)

def schckrow(playerX,row):
	if sumrow(playerX,row)>0 and searchopprow(playerX,row)>0:
		score = fchckrow(playerX,row) + 1
		return score
	else:
		return 0

def tchckrow(playerX,row):
	if sumrow(playerX,row)>0 and searchopprow(playerX,row)>1:
		score = fchckrow(playerX,row) + 10
		return score
	else:
		return 0

def allchckrow(playerX,row):
	allscore = fchckrow(playerX,row) + schckrow(playerX,row) + tchckrow(playerX,row)
	return allscore

def rowscore(playerX):
	total = 0
	for row in board:
		total = total + allchckrow(playerX,row)
	return total

#DEFINE COL WEIGHTAGES
def sumcol(playerX,colindex):
	i = 0
	for rowindex in range(3):
		if board[rowindex][colindex] == playerX:
			i +=1
	return i

def searchoppcol(playerX,colindex):
	if playerX == 1:
		i = 0
		for rowindex in range(3):
			if board[rowindex][colindex] == 2:
				i +=1
		return i
	if playerX == 2:
		i = 0
		for rowindex in range(3):
			if board[rowindex][colindex] == 1:
				i +=1
		return i

def fchckcol(playerX,colindex):
	if searchoppcol(playerX,colindex)>0:
		return 0
	else:
		if sumcol(playerX,colindex) ==2:
			return 3
		else: 
			return sumcol(playerX,colindex)

def schckcol(playerX,colindex):
	if sumcol(playerX,colindex)>0 and searchoppcol(playerX,colindex)>0:
		score = fchckcol(playerX,colindex) + 1
		return score
	else:
		return 0

def tchckcol(playerX,colindex):
	if sumcol(playerX,colindex)>0 and searchoppcol(playerX,colindex)>1:
		score = fchckcol(playerX,colindex) + 10
		return score
	else:
		return 0

def allchckcol(playerX,colindex):
	allscore = fchckcol(playerX,colindex) + schckcol(playerX,colindex) + tchckcol(playerX,colindex)
	return allscore

def colscore(playerX):
	total = 0
	for colindex in range(3):
		total = total + allchckcol(playerX,colindex)
	return total


#DEFINE DIAG WEIGHTAGES
def sumdiag(playerX,diagdir):
	if diagdir == 0:
		score = 0
		for i in range(3):
			if board[i][i] == playerX:
				score +=1
		return score
	elif diagdir == 1:
		score = 0
		for i in range(3):
			if board[i][2-i] == playerX:
				score +=1
		return score

def searchoppdiag(playerX,diagdir):
	if diagdir == 0:
		if playerX == 1:
			score = 0
			for i in range(3):
				if board[i][i] == 2:
					score +=1
			return score
		if playerX == 2:
			score = 0
			for i in range(3):
				if board[i][i] == 1:
					score +=1
			return score
	elif diagdir == 1:
		if playerX == 1:
			score = 0
			for i in range(3):
				if board[i][2-i] == 2:
					score +=1
			return score
		if playerX == 2:
			score = 0
			for i in range(3):
				if board[i][2-i] == 1:
					score +=1
			return score

def fchckdiag(playerX,diagdir):
	if searchoppdiag(playerX,diagdir)>0:
		return 0
	else:
		if sumdiag(playerX,diagdir) ==2:
			return 3
		else: 
			return sumdiag(playerX,diagdir)

def schckdiag(playerX,diagdir):
	if sumdiag(playerX,diagdir)>0 and searchoppdiag(playerX,diagdir)>0:
		score = fchckdiag(playerX,diagdir) + 1
		return score
	else:
		return 0

def tchckdiag(playerX,diagdir):
	if sumdiag(playerX,diagdir)>0 and searchoppdiag(playerX,diagdir)>1:
		score = fchckdiag(playerX,diagdir) + 10
		return score
	else:
		return 0

def allchckdiag(playerX,diagdir):
	allscore = fchckdiag(playerX,diagdir) + schckdiag(playerX,diagdir) + tchckdiag(playerX,diagdir)
	return allscore

def diagscore(playerX):
	total = 0
	for diagdir in range(2):
		total = total + allchckdiag(playerX,diagdir)
	return total

#DEFINE TOTAL SCORE
def score(playerX):
	totscore = rowscore(playerX)+colscore(playerX)+diagscore(playerX)
	return totscore

#RUN THROUGH ALL SCENARIOS

def scenario(playerX,row,col):
	board2 = copy.deepcopy(board)
	board2[row][col] = playerX
	

def AIprog(playerX):
	table = []
	for row in range(3):
		for col in range(3):
			if board[row][col] == 0:
				print "RUN SCENARIO, SAVE SCORE, SAVE ROW/COL position"
			else: pass
	return "BEST POSITION TO TAKE"

board2 = copy.deepcopy(board)
board2[1][0] = 1
print board
print board2
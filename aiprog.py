#AI PROGRAM
r1 = [0,0,1]
r2 = [2,2,1]
r3 = [1,0,2]

board = [r1,r2,r3]

import copy

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
	elif sumrow(playerX,row) ==2:
		return 3
	elif sumrow(playerX,row) ==3:
		return 300
	else: 	
		return sumrow(playerX,row)

def schckrow(playerX,row):
	if sumrow(playerX,row)>0 and searchopprow(playerX,row)>0:
		score = fchckrow(playerX,row) + 2
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

def rowscore(playerX,board2):
	total = 0
	for row in board2:
		total = total + allchckrow(playerX,row)
	return total

#DEFINE COL WEIGHTAGES
def sumcol(playerX,colindex,board2):
	i = 0
	for rowindex in range(3):
		if board2[rowindex][colindex] == playerX:
			i +=1
	return i

def searchoppcol(playerX,colindex,board2):
	if playerX == 1:
		i = 0
		for rowindex in range(3):
			if board2[rowindex][colindex] == 2:
				i +=1
		return i
	if playerX == 2:
		i = 0
		for rowindex in range(3):
			if board2[rowindex][colindex] == 1:
				i +=1
		return i

def fchckcol(playerX,colindex,board2):
	if searchoppcol(playerX,colindex,board2)>0:
		return 0
	elif sumcol(playerX,colindex,board2) ==2:
		return 3
	elif sumcol(playerX,colindex,board2) ==3:
		return 300
	else: 
		return sumcol(playerX,colindex,board2)

def schckcol(playerX,colindex,board2):
	if sumcol(playerX,colindex,board2)>0 and searchoppcol(playerX,colindex,board2)>0:
		score = fchckcol(playerX,colindex,board2) + 2
		return score
	else:
		return 0

def tchckcol(playerX,colindex,board2):
	if sumcol(playerX,colindex,board2)>0 and searchoppcol(playerX,colindex,board2)>1:
		score = fchckcol(playerX,colindex,board2) + 10
		return score
	else:
		return 0

def allchckcol(playerX,colindex,board2):
	allscore = fchckcol(playerX,colindex,board2) + schckcol(playerX,colindex,board2) + tchckcol(playerX,colindex,board2)
	return allscore

def colscore(playerX,board2):
	total = 0
	for colindex in range(3):
		total = total + allchckcol(playerX,colindex,board2)
	return total


#DEFINE DIAG WEIGHTAGES
def sumdiag(playerX,diagdir,board2):
	if diagdir == 0:
		score = 0
		for i in range(3):
			if board2[i][i] == playerX:
				score +=1
		return score
	elif diagdir == 1:
		score = 0
		for i in range(3):
			if board2[i][2-i] == playerX:
				score +=1
		return score

def searchoppdiag(playerX,diagdir,board2):
	if diagdir == 0:
		if playerX == 1:
			score = 0
			for i in range(3):
				if board2[i][i] == 2:
					score +=1
			return score
		if playerX == 2:
			score = 0
			for i in range(3):
				if board2[i][i] == 1:
					score +=1
			return score
	elif diagdir == 1:
		if playerX == 1:
			score = 0
			for i in range(3):
				if board2[i][2-i] == 2:
					score +=1
			return score
		if playerX == 2:
			score = 0
			for i in range(3):
				if board2[i][2-i] == 1:
					score +=1
			return score

def fchckdiag(playerX,diagdir,board2):
	if searchoppdiag(playerX,diagdir,board2)>0:
		return 0
	elif sumdiag(playerX,diagdir,board2) ==2:
		return 3
	elif sumdiag(playerX,diagdir,board2) ==3:
		return 300
	else: 
		return sumdiag(playerX,diagdir,board2)

def schckdiag(playerX,diagdir,board2):
	if sumdiag(playerX,diagdir,board2)>0 and searchoppdiag(playerX,diagdir,board2)>0:
		score = fchckdiag(playerX,diagdir,board2) + 2
		return score
	else:
		return 0

def tchckdiag(playerX,diagdir,board2):
	if sumdiag(playerX,diagdir,board2)>0 and searchoppdiag(playerX,diagdir,board2)>1:
		score = fchckdiag(playerX,diagdir,board2) + 10
		return score
	else:
		return 0

def allchckdiag(playerX,diagdir,board2):
	allscore = fchckdiag(playerX,diagdir,board2) + schckdiag(playerX,diagdir,board2) + tchckdiag(playerX,diagdir,board2)
	return allscore

def diagscore(playerX,board2):
	total = 0
	for diagdir in range(2):
		total = total + allchckdiag(playerX,diagdir,board2)
	return total

#DEFINE TOTAL SCORE
def score(playerX,board2):
	totscore = rowscore(playerX,board2)+colscore(playerX,board2)+diagscore(playerX,board2)
	return totscore

#RUN THROUGH ALL SCENARIOS

def scenario(playerX,board2):
	return score(playerX,board2)

def AIprogrun(playerX):
	table = []
	for row in range(3):
		for col in range(3):
			if board[row][col] == 0:
				board2 = copy.deepcopy(board)
				board2[row][col] = playerX
				table.append([row,col,scenario(playerX,board2)])
			else: pass
	print table

	scores = []
	for i in range(len(table)):
		scores.append(table[i][2])
	topscore = max(scores)
	print topscore

	coordinates = []
	for i in range(len(table)):
		if table[i][2]==topscore:
			coordinates.append(table[i][0])
			coordinates.append(table[i][1])
			break
	print coordinates
	return coordinates

def AIprog(playerX):
	if playerX==2 and (board == [[1,0,0],[0,2,0],[0,0,1]] or board == [[0,0,1],[0,2,0],[1,0,0]]):
			print [1,0]
			return [1,0]
	else: 
		AIprogrun(playerX)

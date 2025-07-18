import copy
from collections import deque
import sys

infinity = 1e9

class GameState:

	def __init__(self, board, player):
		self.board = self.board
		self.player = player

	def __init__(self):
		self.board = [
			['r', 'n', 'r','n', 'r', 'n','r', 'n'],
			['n', 'r', 'n','r', 'n', 'r','n', 'r'],
			['r', 'n', 'r','n', 'r', 'n','r', 'n'],
			['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			['n', 'b', 'n','b', 'n', 'b','n', 'b'],
			['b', 'n', 'b','n', 'b', 'n','b', 'n'],
			['n', 'b', 'n','b', 'n', 'b','n', 'b'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'r','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'b','n', 'R', 'n','n', 'n'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
			#['n', 'n', 'n','n', 'n', 'n','n', 'n'],
		]
		self.player = 1

	def __str__(self):
		retval = ""
		for i in range(8):
			retval += str(self.board[i]) + '\n'
		return retval

	def successor(self, board, player):
		next_states = []
		for i in range(8):
			for j in range(8):
				if (board[i][j] == 'b' or board[i][j] == 'B') and player == 1:
					next_state = copy.deepcopy(board)
					if(-1 < i-1 < 8 and -1 < j-1 < 8 and next_state[i-1][j-1] == 'n' and not self.captureExists(1)):
						next_state[i][j] = 'n'
						if board[i][j] == 'b':
							next_state[i-1][j-1] = 'b'
							if i - 1 == 0:
								next_state[i-1][j-1] = 'B'
						else: next_state[i-1][j-1] = 'B'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i-1 < 8 and -1 < j+1 < 8 and next_state[i-1][j+1] == 'n' and not self.captureExists(1)):
						next_state[i][j] = 'n'
						if board[i][j] == 'b': 
							next_state[i-1][j+1] = 'b'
							if i - 1 == 0:
								next_state[i-1][j+1] = 'B'
						else: next_state[i-1][j+1] = 'B'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'B' and -1 < i+1 < 8 and -1 < j-1 < 8 and next_state[i+1][j-1] == 'n' and not self.captureExists(1)):
						next_state[i][j] = 'n'
						next_state[i+1][j-1] = 'B'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'B' and -1 < i+1 < 8 and -1 < j+1 < 8 and next_state[i+1][j+1] == 'n' and not self.captureExists(1)):
						next_state[i][j] = 'n'
						next_state[i+1][j+1] = 'B'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and next_state[i-1][j-1].lower() == 'r' and next_state[i-2][j-2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i-1][j-1] = 'n'
						if board[i][j] == 'b':
							next_state[i-2][j-2] = 'b'
							if i - 2 == 0:
								next_state[i-2][j-2] = 'B'
						else:
							next_state[i-2][j-2] = 'B'
						if self.hasCapture(next_state, 1, i-2, j-2):
							listOfCaptures = self.getCaptures(next_state, 1, i-2, j-2)
						#next_states.append(next_state)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and next_state[i-1][j+1].lower() == 'r' and next_state[i-2][j+2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i-1][j+1] = 'n'
						if board[i][j] == 'b':
							next_state[i-2][j+2] = 'b'
							if i - 2 == 0:
								next_state[i-2][j+2] = 'B'
						else:
							next_state[i-2][j+2] = 'B'
						if self.hasCapture(next_state, 1, i-2, j+2):
							listOfCaptures = self.getCaptures(next_state, 1, i-2, j+2)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'B' and -1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and next_state[i+1][j-1].lower() == 'r' and next_state[i+2][j-2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i+1][j-1] = 'n'
						next_state[i+2][j-2] = 'B'
						if self.hasCapture(next_state, 1, i+2, j-2):
							listOfCaptures = self.getCaptures(next_state, 1, i+2, j-2)
						#next_states.append(next_state)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'B' and -1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and next_state[i+1][j+1].lower() == 'r' and next_state[i+2][j+2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i+1][j+1] = 'n'
						next_state[i+2][j+2] = 'B'
						if self.hasCapture(next_state, 1, i+2, j+2):
							listOfCaptures = self.getCaptures(next_state, 1, i+2, j+2)
						#next_states.append(next_state)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
				if board[i][j].lower() == 'r' and player == -1:
					next_state = copy.deepcopy(board)
					if(-1 < i+1 < 8 and -1 < j-1 < 8 and next_state[i+1][j-1] == 'n' and not self.captureExists(-1)):
						next_state[i][j] = 'n'
						if board[i][j] == 'r':
							next_state[i+1][j-1] = 'r'
							if i+1 == 7:
								next_state[i+1][j-1] = 'R'
						else:
							next_state[i+1][j-1] = 'r'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i+1 < 8 and -1 < j+1 < 8 and next_state[i+1][j+1] == 'n' and not self.captureExists(-1)):
						next_state[i][j] = 'n'
						if board[i][j] == 'r':
							next_state[i+1][j+1] = 'r'
							if i + 1 == 7:
								next_state[i+1][j+1] = 'R'
						else:
							next_state[i+1][j+1] = 'R'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'R' and -1 < i-1 < 8 and -1 < j-1 < 8 and next_state[i-1][j-1] == 'n' and not self.captureExists(-1)):
						next_state[i][j] = 'n'
						next_state[i-1][j-1] = 'R'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'R' and -1 < i-1 < 8 and -1 < j+1 < 8 and next_state[i-1][j+1] == 'n' and not self.captureExists(-1)):
						next_state[i][j] = 'n'
						next_state[i-1][j+1] = 'R'
						next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and next_state[i+1][j-1].lower() == 'b' and next_state[i+2][j-2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i+1][j-1] = 'n'
						if board[i][j] == 'r':
							next_state[i+2][j-2] = 'r'
							if i + 2 == 7:
								next_state[i+2][j-2] = 'R'
						else:
							next_state[i+2][j-2] = 'R'
						if self.hasCapture(next_state, -1, i+2, j-2):
							listOfCaptures = self.getCaptures(next_state, -1, i+2, j-2)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'R' and -1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and next_state[i-1][j-1].lower() == 'b' and next_state[i-2][j-2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i-1][j-1] = 'n'
						next_state[i-2][j-2] = 'R'
						if self.hasCapture(next_state, -1, i-2, j-2):
							listOfCaptures = self.getCaptures(next_state, -1, i-2, j-2)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(board[i][j] == 'R' and -1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and next_state[i-1][j+1].lower() == 'b' and next_state[i-2][j+2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i-1][j+1] = 'n'
						next_state[i-2][j+2] = 'R'
						if self.hasCapture(next_state, -1, i-2, j+2):
							listOfCaptures = self.getCaptures(next_state, -1, i-2, j+2)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					next_state = copy.deepcopy(board)
					if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and next_state[i+1][j+1].lower() == 'b' and next_state[i+2][j+2] == 'n'):
						next_state[i][j] = 'n'
						next_state[i+1][j+1] = 'n'
						if board[i][j] == 'r':
							next_state[i+2][j+2] = 'r'
							if i + 2 == 7:
								next_state[i+2][j+2] = 'R'
						else:
							next_state[i+2][j+2] = 'R'
						if self.hasCapture(next_state, -1, i+2, j+2):
							listOfCaptures = self.getCaptures(next_state, -1, i+2, j+2)
							for m in listOfCaptures:
								next_states.append(m)
						else:
							next_states.append(next_state)
					
					#stack = deque()
					#stack.append([next_state, i, j])
					#while(stack.empty() == False):
						#next_state = stack.pop()
						#if(next_state[0][][])

		return next_states
	
	def getCaptures(self, board, player, i_coord, j_coord):
		stack = []
		results = []
		stack.append((copy.deepcopy(board), i_coord, j_coord))
		if player == 1:
			while len(stack) != 0:
				changed = False
				next_state, i, j = stack.pop()
				if(next_state[i][j].lower() == 'b' and -1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and next_state[i-1][j-1].lower() == 'r' and next_state[i-2][j-2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i-1][j-1] = 'n'
					if next_state[i][j] == 'b':
						new_state[i-2][j-2] = 'b'
						if i - 2 == 0:
							new_state[i-2][j-2] = 'B'
					else:
						new_state[i-2][j-2] = 'B'
					stack.append((copy.deepcopy(new_state), i-2, j-2))
					changed = True
				if(next_state[i][j].lower() == 'b' and -1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and next_state[i-1][j+1].lower() == 'r' and next_state[i-2][j+2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i-1][j+1] = 'n'
					if next_state[i][j] == 'b':
						new_state[i-2][j+2] = 'b'
						if i - 2 == 0:
							new_state[i-2][j+2] = 'B'
					else:
						new_state[i-2][j+2] = 'B'
					stack.append((copy.deepcopy(new_state), i-2, j+2))
					changed = True
				if(next_state[i][j] == 'B' and -1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and next_state[i+1][j-1].lower() == 'r' and next_state[i+2][j-2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i+1][j-1] = 'n'
					new_state[i+2][j-2] = 'B'
					stack.append((copy.deepcopy(new_state), i+2, j-2))
					changed = True
				if(next_state[i][j] == 'B' and -1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and next_state[i+1][j+1].lower() == 'r' and next_state[i+2][j+2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i+1][j+1] = 'n'
					new_state[i+2][j+2] = 'B'
					stack.append((copy.deepcopy(new_state), i+2, j+2))
					changed = True
				if not changed:
					results.append(next_state)
		elif player == -1:
			while len(stack) != 0:
				changed = False
				next_state, i, j = stack.pop()
				if(next_state[i][j].lower() == 'r' and -1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and next_state[i+1][j-1].lower() == 'b' and next_state[i+2][j-2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i+1][j-1] = 'n'
					if next_state[i][j] == 'r':
						new_state[i+2][j-2] = 'r'
						if i + 2 == 7:
							new_state[i+2][j-2] = 'R'
					else:
						new_state[i+2][j-2] = 'R'
					stack.append((copy.deepcopy(new_state), i+2, j-2))
					changed = True
				if(next_state[i][j].lower() == 'r' and -1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and next_state[i+1][j+1].lower() == 'b' and next_state[i+2][j+2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i+1][j+1] = 'n'
					if next_state[i][j] == 'r':
						new_state[i+2][j+2] = 'r'
						if i + 2 == 7:
							new_state[i+2][j+2] = 'R'
					else:
						new_state[i+2][j+2] = 'R'
					stack.append((copy.deepcopy(new_state), i+2, j+2))
					changed = True
				if(next_state[i][j] == 'R' and -1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and next_state[i-1][j-1].lower() == 'b' and next_state[i-2][j-2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i-1][j-1] = 'n'
					new_state[i-2][j-2] = 'R'
					stack.append((copy.deepcopy(new_state), i-2, j-2))
					changed = True
				if(next_state[i][j] == 'R' and -1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and next_state[i-1][j+1].lower() == 'b' and next_state[i-2][j+2] == 'n'):
					new_state = copy.deepcopy(next_state)
					new_state[i][j] = 'n'
					new_state[i-1][j+1] = 'n'
					new_state[i-2][j+2] = 'R'
					stack.append((copy.deepcopy(new_state), i-2, j+2))
					changed = True
				if not changed:
					results.append(next_state)
				


		#return [board]
		#print("hi")
		return results


	def move(self, board, i, j, captureExists):
		ur = None
		ul = None
		ll = None
		lr = None
		if board[i][j] == 'b' or board[i][j] == 'B':
			next_state = copy.deepcopy(board)
			if(-1 < i-1 < 8 and -1 < j-1 < 8 and next_state[i-1][j-1] == 'n' and not captureExists):
				next_state[i][j] = 'n'
				if board[i][j] == 'b':
					next_state[i-1][j-1] = 'b'
				else:
					next_state[i-1][j-1] = 'B'
				ul = next_state
			next_state = copy.deepcopy(board)
			if(-1 < i-1 < 8 and -1 < j+1 < 8 and next_state[i-1][j+1] == 'n' and not captureExists):
				next_state[i][j] = 'n'
				if board[i][j] == 'b':
					next_state[i-1][j+1] = 'b'
				else:
					next_state[i-1][j+1] = 'B'
				ur = next_state
			next_state = copy.deepcopy(board)
			if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and next_state[i-1][j-1] == 'r' and next_state[i-2][j-2] == 'n'):
				next_state[i][j] = 'n'
				next_state[i-1][j-1] = 'n'
				if board[i][j] == 'b':
					next_state[i-2][j-2] = 'b'
				else:
					next_state[i-2][j-2] = 'B'
				ul = next_state
			next_state = copy.deepcopy(board)
			if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and next_state[i-1][j+1] == 'r' and next_state[i-2][j+2] == 'n'):
				next_state[i][j] = 'n'
				next_state[i-1][j+1] = 'n'
				if board[i][j] == 'b':
					next_state[i-2][j+2] = 'b'
				else:
					next_state[i-2][j+2] = 'B'
				ur = next_state
			if board[i][j] == 'B':
				next_state = copy.deepcopy(board)
				if(-1 < i+1 < 8 and -1 < j-1 < 8 and next_state[i+1][j-1] == 'n' and not captureExists):
					next_state[i][j] = 'n'
					next_state[i+1][j-1] = 'B'
					ll = next_state
				next_state = copy.deepcopy(board)
				if(-1 < i+1 < 8 and -1 < j+1 < 8 and next_state[i+1][j+1] == 'n' and not captureExists):
					next_state[i][j] = 'n'
					next_state[i+1][j+1] = 'B'
					lr = next_state
				next_state = copy.deepcopy(board)
				if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and next_state[i+1][j-1] == 'r' and next_state[i+2][j-2] == 'n'):
					next_state[i][j] = 'n'
					next_state[i+1][j-1] = 'n'
					next_state[i+2][j-2] = 'B'
					ll = next_state
				next_state = copy.deepcopy(board)
				if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and next_state[i+1][j+1] == 'r' and next_state[i+2][j+2] == 'n'):
					next_state[i][j] = 'n'
					next_state[i+1][j+1] = 'n'
					next_state[i+2][j+2] = 'B'
					lr = next_state

		return {'upper right': ur, 'upper left': ul, 'lower right': lr, 'lower left': ll}

	def eval(self, board=None):
		if board == None: board = self.board
		if board == 1:
			return 1
		if board == -1:
			return -1
		numB = 0
		numR = 0
		numB_king = 0
		numR_king = 0
		for i in range(8):
			for j in range(8):
				if(board[i][j] == 'b'):
					numB += 1
				elif(board[i][j] == 'r'):
					numR += 1
				elif(board[i][j] == 'B'):
					numB += 1
					numB_king += 1
				elif(board[i][j] == 'R'):
					numR_king += 1
		if(numB == 0):
			return -50
		elif(numR == 0):
			return 50
		else:
			return numB + numB_king - numR - numR_king

	def minimax_eval(self, board, max=True, depth=20):
		current_score = self.eval(board)
		if current_score == 50: return infinity
		elif current_score == -50: return -infinity
		if(depth == 0):
			return current_score
		if max:
			best_score = -infinity
		else:
			best_score = infinity
		for next_board in self.successor(board, 1 if max else -1):
			score = self.minimax_eval(next_board, not max, depth-1)
			if (max and score > best_score): best_score = score
			elif (not max and score < best_score): best_score = score
		return best_score

	def minimax_play(self, max=True):
		best_move = -1
		if max:
			best_score = -infinity
		else:
			best_score = infinity
		states = list(enumerate(self.successor(self.board, 1 if max else -1)))
		for i,next_board in states:
			score = self.minimax_eval(next_board, max, 3)
			if (max and score > best_score): 
				best_score = score
				best_move = i
			elif (not max and score < best_score):
				best_score = score
				best_move = i
		if len(states) == 0 and max:
			return -1
		elif len(states) == 0 and not max:
			return 1
		else:
			return states[best_move][1]
	
	def print(self):
		# Print Board
		RED_BRIGHT = '\033[91m'
		RED_DARK = '\033[1;91m'
		BLUE_BRIGHT = '\033[94m'
		BLUE_DARK = '\033[1;94m'
		ENDC = '\033[0m'
		print("    a   b   c   d   e   f   g   h")
		print("  +---+---+---+---+---+---+---+---+")
		for i in range(8):
			rowLabel = i + 1
			row = "" + str(rowLabel) + " |"
			for j in range(8):
				checker = self.board[i][j]
				if checker == 'r':
					row += " " + RED_BRIGHT + str(checker) + ENDC + " |"
				elif checker == 'R':
					row += " " + RED_DARK + str(checker) + ENDC + " |"
				elif checker == 'b':
					row += " " + BLUE_BRIGHT + str(checker) + ENDC + " |"
				elif checker == 'B':
					row += " " + BLUE_DARK + str(checker) + ENDC + " |" 
				else:
					row += "   |" 
			print(row)
			print("  +---+---+---+---+---+---+---+---+")

	def captureExists(self, player):
		if player == 1:
			for i in range(8):
				for j in range(8):
					if self.board[i][j] == 'b' or self.board[i][j] == 'B':
						if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and (self.board[i-1][j-1] == 'r' or self.board[i-1][j-1] == 'R') and self.board[i-2][j-2] == 'n'):
							return True
						if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and (self.board[i-1][j+1] == 'r' or self.board[i-1][j+1] == 'R') and self.board[i-2][j+2] == 'n'):
							return True
					if self.board[i][j] == 'B':
						if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and (self.board[i+1][j-1] == 'r' or self.board[i+1][j-1] == 'R') and self.board[i+2][j-2] == 'n'):
							return True
						if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and (self.board[i+1][j+1] == 'r' or self.board[i+1][j+1] == 'R') and self.board[i+2][j+2] == 'n'):
							return True
			return False
		elif player == -1:
			for i in range(8):
				for j in range(8):
					if self.board[i][j] == 'r' or self.board[i][j] == 'R':
						if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and (self.board[i+1][j-1] == 'b' or self.board[i+1][j-1] == 'B') and self.board[i+2][j-2] == 'n'):
							return True
						if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and (self.board[i+1][j+1] == 'b' or self.board[i+1][j+1] == 'B') and self.board[i+2][j+2] == 'n'):
							return True
					if self.board[i][j] == 'R':
						if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and (self.board[i-1][j-1] == 'b' or self.board[i-1][j-1] == 'B') and self.board[i-2][j-2] == 'n'):
							return True
						if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and (self.board[i-1][j+1] == 'b' or self.board[i-1][j+1] == 'B') and self.board[i-2][j+2] == 'n'):
							return True
			return False
	
	def hasCapture(self, board, player, i, j):
		if player == 1:
			if board[i][j] == 'b' or board[i][j] == 'B':
				if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and (board[i-1][j-1] == 'r' or board[i-1][j-1] == 'R') and board[i-2][j-2] == 'n'):
					return True
				if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and (board[i-1][j+1] == 'r' or self.board[i-1][j+1] == 'R') and board[i-2][j+2] == 'n'):
					return True
			if board[i][j] == 'B':
				if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and (board[i+1][j-1] == 'r' or board[i+1][j-1] == 'R') and board[i+2][j-2] == 'n'):
					return True
				if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and (board[i+1][j+1] == 'r' or board[i+1][j+1] == 'R') and board[i+2][j+2] == 'n'):
					return True
			return False
		elif player == -1:
			if board[i][j] == 'r' or board[i][j] == 'R':
				if(-1 < i+1 < 8 and -1 < j-1 < 8 and -1 < i+2 < 8 and -1 < j-2 < 8 and (board[i+1][j-1] == 'b' or board[i+1][j-1] == 'B') and board[i+2][j-2] == 'n'):
					return True
				if(-1 < i+1 < 8 and -1 < j+1 < 8 and -1 < i+2 < 8 and -1 < j+2 < 8 and (board[i+1][j+1] == 'b' or board[i+1][j+1] == 'B') and board[i+2][j+2] == 'n'):
					return True
			if board[i][j] == 'R':
				if(-1 < i-1 < 8 and -1 < j-1 < 8 and -1 < i-2 < 8 and -1 < j-2 < 8 and (board[i-1][j-1] == 'b' or board[i-1][j-1] == 'B') and board[i-2][j-2] == 'n'):
					return True
				if(-1 < i-1 < 8 and -1 < j+1 < 8 and -1 < i-2 < 8 and -1 < j+2 < 8 and (board[i-1][j+1] == 'b' or board[i-1][j+1] == 'B') and board[i-2][j+2] == 'n'):
					return True
			return False

	def playerCannotMove(self):
		if len(self.successor(self.board, 1)) == 0:
			return True
		return False


def play_vs_computer():
	state = GameState()
	while(True):
		state.print()
		if state.eval() == 50:
			print("Player wins")
			break
		elif state.eval() == -50:
			print("Computer wins")
			break
		chosen = ''
		choice = None
		valid = False
		captureExists = state.captureExists(1) # 1 means the player (not the bot, which is -1)
		while((chosen != 'b' and chosen != 'B') or not valid):
			if state.playerCannotMove():
				print("Computer wins")
				sys.exit()
			if captureExists:
				print("CAPTURE DETECTED")
				stillHasCaptures = True
			inp = input("Choose a piece (i.e. b4): ")
			try:
				cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
				i = int(inp[1]) - 1
				j = cols.index(inp[0])
				chosen = state.board[i][j]
				print('chosen', chosen)
				if(chosen != 'b' and chosen != 'B'):
					print('Invalid piece')
				temp = state.move(state.board, i,j, captureExists)
				if temp['upper left'] is None and temp['upper right'] is None and temp['lower left'] is None and temp['lower right'] is None:
					print('Piece does not have any available moves')
				# Check if it has captures if there is a capture
				elif captureExists and not state.hasCapture(state.board, 1, i, j):
					print('You must select a piece that can capture')
				else:
					valid = True
				
			except:
				print('Invalid piece')
		while(choice == None or stillHasCaptures):
			if state.hasCapture(state.board, 1, i, j):
				inp = str(input("Choose a capture (upper left, upper right): "))
			else:
				inp = str(input("Choose where to move to (upper left, upper right): "))
			dict = state.move(state.board, i,j, captureExists)
			if inp in dict:
				if dict[inp] is not None:
					choice = dict[inp]
					if captureExists:
						if inp == "upper left":
							i -= 2
							j -= 2
						if inp == "upper right":
							i -= 2
							j += 2
						if inp == "lower left":
							i += 2
							j -= 2
						if inp == "lower right":
							i += 2
							j += 2
					else:
						if inp == "upper left":
							i -= 1
							j -= 1
						if inp == "upper right":
							i -= 1
							j += 1
						if inp == "lower left":
							i += 1
							j -= 1
						if inp == "lower right":
							i += 1
							j += 1
					state.board = choice
					if i == 0:
						state.board[i][j] = 'B'
					if captureExists and state.hasCapture(state.board, 1, i, j):
						stillHasCaptures = True
						state.print()
						print("You have a follow-up capture")
					else:
						stillHasCaptures = False
			else:
				choice = None

		state.print()

		if state.eval() == 50:
			print("Player wins")
			break
		elif state.eval() == -50:
			print("Computer wins")
			break
		state.board = state.minimax_play(max=False)
		if state.eval() == 50:
			print("Player wins")
			break
		elif state.eval() == -50:
			state.print()
			print("Computer wins")
			break

play_vs_computer()
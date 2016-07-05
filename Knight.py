from ChessPiece import ChessPiece
from main import *

class Knight(ChessPiece):

	def __init__(self, row, col, team_color):
		super().__init__

	def move(self,row, col):
		if(self.possible_move(row,col)):
			if((abs(self.col-col) == 2 and abs(self.row-row) == 1) or (abs(self.col-col) == 1 and abs(self.row-row) == 2) ):
				siege(row,col,self)
			else:
				print('Invalid Move')
				return(False)
		else:
			print('Invalid Move')
			return(False)
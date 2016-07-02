from ChessPiece import ChessPiece
from main import *

class Rook(ChessPiece):

	def __init__(self, row, col, team_color):
		super().__init__

	def check_for_one_direction(row,col):

	def move(row_col):
		# Rooks can move in all cardinal directions, but only ONE direction at once
		# e.g. the difference between position can be whatever but in one row dir, or one col dir
		# Need a succint way to say yes, if it's less than row that's cool, but not if it is changing self.row or self.col
		if (check_for_one_direction == True and check_for_has_piece(row,col) == True and chessboard[row][col].team_color !== self.team_color)
			return siege(row,col)

		return(False)

from ChessPiece import ChessPiece

class Pawn(ChessPiece):

	def __init__(self, row, col, team_color):
		super().__init__

	def check_diagonal(row, col):
		if (col == self.col - 1 or col == self.col + 1):
			return(True)
		return(False)

	def move(row, col):
		if (row == self.row + 1 and self.team_color == 'red'):

			if(self.check_diagonal(row,col) == True):
				piece_exists = check_for_has_piece(row,col)

				if (piece_exists):
					return siege(row,col)
				else:
					print("Invalid move")
					return(False)

			elif (self.check_diagonal(row,col) == False and check_for_has_piece(row,col) == False):
				return siege(row,col)

		if (row == self.row - 1 and self.team_color == 'white'):

			if(self.check_diagonal(row,col) == True):
				piece_exists = check_for_has_piece(row,col)

				if (piece_exists):
					return siege(row,col)
				else:
					print("Invalid move")
					return(False)

			elif (self.check_diagonal(row,col) == False and check_for_has_piece(row,col) == False):
				chessboard(row,col) = self
				print("Moved to " + row + " , " + col)
				return(True)

		return(error())

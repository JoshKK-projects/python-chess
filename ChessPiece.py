class ChessPiece:
    """ Standard chess piece properties with row, column position """
    def __init__(self, row, col, team_color)#suggestion - team_color be 1 or -1 so it can be used to determine allowed pawn Y direction
    	self.row = row
	    self.col = col
	    self.team_color = team_color
	def possible_move(self,row,col):
		if(board[row][col] != 0 and board[row][col].team_color == self.team_color):
			return(False)
		if(row>7 or row<0 or col>7 or col<0):
			return(False)
		return(True)


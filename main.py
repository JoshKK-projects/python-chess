chessboard = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0]]

 def siege(row,col,piece):
	chessboard(row,col) = piece
	print("Moved to " + row + " , " + col)
	return(True)

def error():
	print("Invalid move")
	return(False)

def check_for_has_piece(row,col):
	if (chessboard(row, col) != 0)
		return True
	return False

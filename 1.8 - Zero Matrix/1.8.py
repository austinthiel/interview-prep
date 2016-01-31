# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zeroMatrix(A):
	rows = len(A)
	cols = len(A[0])							# assuming the array is not jagged
	rowStor = []
	colStor = []
	for j in range(cols):
		for i in range(rows):
			if A[i][j] == 0:
				if i not in rowStor:			# avoid storing duplicate rows
					rowStor.append(i)		# store the row position to zero out later
				if j not in colStor:			# avoid storing duplicate columns
					colStor.append(j)		# same with the column position in a separate array
	for row in rowStor:
		for j in range(cols):
			A[row][j] = 0;					# zero out the rows we know have zeroes in them
	for col in colStor:
		for i in range(rows):
			A[i][col] = 0;					# and do the same with the columns
	return A;

A1 = [[1,0,1,0], [2,2,0,2], [3,3,3,3]]					# Test Case 1 ([[0,0,0,0],[0,0,0,0],[3,0,0,0]])
print(zeroMatrix(A1))

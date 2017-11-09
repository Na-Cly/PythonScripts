#!Python 
#Author: Derek Schmell
#Description: Tests a matrix in Python

#Matrix is defined by defining lists inside of a list.
#A matrix in Python does not have to be defined evenly per row, but please for your sake make it even.
matrix = [["Row 0:Column 0", "Row 0:Column 1","Row 0:Column 2"],["Row 1:Column 0", "Row 1:Column 1", "Row 1:Column 2"],["Row 2:Column 0","Row 2:Column 1", "Row 2:Column 2"]]
#Another Matrix
#matrix = [["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"]]

#It will behoove you to make a max length variable as finding the len() of a matrix is not as straightforward as you typing in the size that you made it into a variable.

#If you put size of 3 for there being 3 elements, remember that your max index number is 2. Also remember that a loop that runs from 0 - 3 runs for 0,1,2
matrixSize = 3

#other matrix size
#matrixSize = 7

print("\n\n\n\n")

#Prints the element at space 0 - 0
print(matrix[0][0])

#Prints the element at space 0 - 2
print(matrix[0][2])

print("\n\n---------------------------------------------------------\n\n")

#An example of looping through the matrix.
#A traditional list only requires 1 loop to traverse, but a matrix requires 2. An outer loop to traverse the rows, and an inner loop to traverse the columns.
for r in range(matrixSize):
	#don't need to do anything here when just printing.
	#r in the outer loop will represent the row number.
	for c in range(matrixSize):
		#c represents columns in case you haven't caught on yet ;)
		print(matrix[r][c],end = "\t")
	print()	
#if you need another example of how this helps you. Uncomment the 2nd matrix defition and comment out the first.
#also change the matrixSize to 7 if you're using the other matrix.
	
	
	

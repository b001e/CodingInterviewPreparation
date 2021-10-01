#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

#	 _ _ _           _ _ _
#	|1 2 3 |        |7 4 1 |
#	|4 5 6 | --->   |8 5 2 |
#	|7 8 9 |        |9 6 3 |
#	 - - -           - - - 



# Approach 
#	1. We will start be moving the corners of the matrix, but for terms of saving ourselves storing a lot of temporary variables,
# 	   we will store only the top left corner as a temporary value and swap the numbers counter clock-wise
# 	   so we will store 1 in a temporary value and swap 1 with 7, then swap the 7 in the bottom left with the 9 in the bottom right.
#	   after that we will swap the 3 in the top right with the 9 in the bottom right, and finally swap the 3 in the top right with our
#      temporary value that is 1.
#	2. update right, left, top, and bottom variables to match the numbers that come next in the loop

matrix = [[1,2,3],[4,5,6],[7,8,9]]


def rotateImage(matrix):

	left, right = 0, len(matrix)-1


	while left < right:

		for i in range(right - left): # right - left because we are stopping 1 before the end of our column
			top, bottom = left, right


			topLeft = matrix[top][left +i]

			# top left --> bottom left
			matrix[top][left+i] = matrix[bottom-i][left]

			# bottom left --> bottom right
			matrix[bottom -i][left] = matrix[bottom][right-i]
			# bottom right --> top right
			matrix[bottom][right-i] = matrix[top+i][right]
			# top right --> top left
			matrix[top+i][right] = topLeft


		left+=1
		right-=1
	return matrix
print(f"Original matrix --> {matrix}. Rotated matrix --> {rotateImage(matrix)}")




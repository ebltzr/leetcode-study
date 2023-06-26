# https://leetcode.com/problems/set-matrix-zeroes/

[0,0,0]
[0,1,0]
[0,0,0]




def setZeroes(self, matrix):
#first for loop is to access list themseleves from in our matrix
# in a maxtrix will start with two for loops if you know it's not a  O(n^2)
    col = 0 # -> index
    row = 0  # -> index
    for i in range(len(matrix)):
        for j in range(len(matrix(0))):
            # if matrix[i][j] == 1 -- iterate thru individual elements
            # search left and right, in one direction use one for loop
            list = []
        # search only right hand side of row
        # if matrix[row:]:
            list.extend(matrix[row[col:]])
        
                    # list = [1,2,3]
                    # list2 = [4,5,6]
                    # lst2.extend = [1,2,3,4,5,6]
        
            for elem in list:
                if elem == 1:
                    return True

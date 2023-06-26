# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
        
#         # we are searching for 0's
#         row = []
#         col = []
        
        # this is how to start for any matrix problem, two for loops
        # for i in range(len(matrix)):
        #     for j in range(len(matrix(0))):
        #         if matrix[i][j] == 0:
        #             row = i
        #             col = j
                    
        # matrix[row] = [0] = (len(matrix[row]))
        
        # for k in range(len(matrix)):
        #     matrix[k][col] = 0
            
            
    ####### pass first test case
    
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # we are searching for 0's
        rows = []
        cols = []
    
        for i in range(len(matrix)):
            for j in range(len(matrix(0))):
                if matrix[i][j] == 0:
                    rows.append = i
                    cols.append = j
        for row in rows:  
            matrix[row] = [0] * (len(matrix[row]))
        
        for k in range(len(matrix)):
            # this changes every 0 in columns
            for col in cols:
                matrix[k][col] = 0  
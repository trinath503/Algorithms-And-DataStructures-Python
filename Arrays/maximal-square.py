class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return -1 
        
        if matrix and len(matrix[0]) ==0:
            return -1
        
        rows, cols = len(matrix) , len(matrix[0])
        
        dp = [ [0 for _ in range(cols+1)] for _ in range(rows+1) ]
         
        max_area = 0
        
        for row_index in range(1, rows+1):
            
            for col_index in range(1, cols+1):
                
                if matrix[row_index-1][col_index-1] == '1':
                    dp[row_index][col_index] = min(
                        dp[row_index][col_index-1],
                        dp[row_index-1][col_index-1],
                        dp[row_index-1][col_index]
                    ) + 1
                    max_area = max(max_area, dp[row_index][col_index])
                    
        return max_area*max_area
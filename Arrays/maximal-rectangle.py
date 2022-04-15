class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        global_max_area = 0
        
        # base matrix 
        if not matrix or len(matrix[0])==0:
            return global_max_area
        rows, cols = len(matrix), len(matrix[0])
        
        heights = [0] * cols
        # print(heights)
        
        for row in matrix:
            
            # convert row to histogram 
            for i in range(cols):
                # print(i, row)
                heights[i] = heights[i]+1 if row[i] == '1' else 0
            
            # find the largest rectangle from row-histogram 
            
            stack = []
            max_area = 0
            print(heights)
            # process elements to end if elements in increasing order
            for index, curr_height in enumerate(heights):
                start_index = index 

                while stack and stack[-1][1] > curr_height:

                    pop_index, pop_height = stack.pop()

                    width = index - pop_index
                    max_area = max(max_area, width * pop_height )
                    start_index = pop_index 

                stack.append((start_index, curr_height))

            total_heights = len(heights)

            # remaning elements in stack
            for i, h in stack:
                width = (total_heights -i)
                max_area = max(max_area,  width*h )


            if global_max_area < max_area:
                global_max_area = max_area
        
        return global_max_area
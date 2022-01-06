class Solution:
	
	def is_valid_and_rotten(self, arr, i, j, r,c):
		return i>0 and j<c and arr[i][j]!=2
	
	def find_rotten_apples(self,grid, i,j, r,c, visited):
		for direcion in []:
			x,y = direcion
			if is_valid_and_rotten(grid, i, j, r,c):
				visited[x][y] = True
				self.find_rotten_apples(grid, x,y, r,c, visited)
		
		
		
	def getDaysToRot(self, grid: List[List[int]]) -> int:
		# add your logic here
		
		row, col = len(grid), len(grid[0])
		rotting_apples, fresh_apples = set(), set()
		for i in range(row):
			for j in range(col):
				if grid[i][j] ==2:
					rotting_apples.add((i,j))
				if grid[i][j]==1:
					fresh_apples.add((i,j))
		# rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
		# fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
		total_days = 0
		# print(rotting, fresh)
		while fresh_apples:
			
			if not rotting_apples: 
				return -1
			level_rotten_apples = set()
			for i, j in rotting_apples:
				for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
					if (i+di, j+dj) in fresh_apples:
						level_rotten_apples.add((i+di, j+dj))
					
				
			# rotting_apples = {(i+di, j+dj) for i, j in rotting_apples for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh_apples}
			fresh_apples -= level_rotten_apples
			rotting_apples = level_rotten_apples
			total_days += 1
		return total_days


        # solution-2:
        # def orangesRotting(self, grid: List[List[int]]) -> int:
        #     row, col = len(grid), len(grid[0])
        #     rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        #     fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        #     timer = 0
        #     while fresh:
        #         if not rotting: return -1
        #         rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
        #         fresh -= rotting
        #         timer += 1
        #     return timer

						
					
		



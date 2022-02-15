class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        print(candidates)
        
        result = []
        
        def find_combination_sum_path(previous_index, curent_path, current_sum):
            
            if current_sum > target: return
        
            if current_sum == target:
                result.append(curent_path)
                return 
            
            for current_index in range(previous_index, len(candidates)):
                # to make path unique 
                if current_index > previous_index and candidates[current_index] == candidates[current_index-1]:
                    continue
                print(current_index+1, 
                    curent_path+[candidates[current_index]],
                    current_sum+candidates[current_index])
                # self element can be used only once 
                find_combination_sum_path(
                    current_index+1, 
                    curent_path+[candidates[current_index]],
                    current_sum+candidates[current_index]
                )
                
                
        find_combination_sum_path(0, [], 0)
        
        return result

# input array & target        
# [10,1,2,7,6,1,5]
# 8

# Logs 

"""
[1, 1, 2, 5, 6, 7, 10]
1 [1] 1
2 [1, 1] 2
3 [1, 1, 2] 4
4 [1, 1, 2, 5] 9
5 [1, 1, 2, 6] 10
6 [1, 1, 2, 7] 11
7 [1, 1, 2, 10] 14
4 [1, 1, 5] 7
5 [1, 1, 5, 6] 13
6 [1, 1, 5, 7] 14
7 [1, 1, 5, 10] 17
5 [1, 1, 6] 8
6 [1, 1, 7] 9
7 [1, 1, 10] 12
3 [1, 2] 3
4 [1, 2, 5] 8
5 [1, 2, 6] 9
6 [1, 2, 7] 10
7 [1, 2, 10] 13
4 [1, 5] 6
5 [1, 5, 6] 12
6 [1, 5, 7] 13
7 [1, 5, 10] 16
5 [1, 6] 7
6 [1, 6, 7] 14
7 [1, 6, 10] 17
6 [1, 7] 8
7 [1, 10] 11
3 [2] 2
4 [2, 5] 7
5 [2, 5, 6] 13
6 [2, 5, 7] 14
7 [2, 5, 10] 17
5 [2, 6] 8
6 [2, 7] 9
7 [2, 10] 12
4 [5] 5
5 [5, 6] 11
6 [5, 7] 12
7 [5, 10] 15
5 [6] 6
6 [6, 7] 13
7 [6, 10] 16
6 [7] 7
7 [7, 10] 17
7 [10] 10


"""
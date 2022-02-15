"""
 array of distinct integers candidates and a target integer target
 The same number may be chosen from candidates an unlimited number of times.
 Two combinations are unique if the frequency of at least one of the chosen numbers is different.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        # print(candidates)
        
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
                    
                print(current_index, 
                    curent_path+[candidates[current_index]],
                    current_sum+candidates[current_index])
                
                # self element can be used only once 
                find_combination_sum_path(
                    current_index, 
                    curent_path+[candidates[current_index]],
                    current_sum+candidates[current_index]
                )
                
                
        find_combination_sum_path(0, [], 0)
        
        return result
        
# input data
# [2,3,6,7]
# 7


"""
Logs:
0 [2] 2
0 [2, 2] 4
0 [2, 2, 2] 6
0 [2, 2, 2, 2] 8
1 [2, 2, 2, 3] 9
2 [2, 2, 2, 6] 12
3 [2, 2, 2, 7] 13
1 [2, 2, 3] 7
2 [2, 2, 6] 10
3 [2, 2, 7] 11
1 [2, 3] 5
1 [2, 3, 3] 8
2 [2, 3, 6] 11
3 [2, 3, 7] 12
2 [2, 6] 8
3 [2, 7] 9
1 [3] 3
1 [3, 3] 6
1 [3, 3, 3] 9
2 [3, 3, 6] 12
3 [3, 3, 7] 13
2 [3, 6] 9
3 [3, 7] 10
2 [6] 6
2 [6, 6] 12
3 [6, 7] 13
3 [7] 7
"""
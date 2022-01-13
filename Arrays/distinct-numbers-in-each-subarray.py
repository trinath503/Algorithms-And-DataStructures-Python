"""

distinct_numbers {'count': 2, 1: 1, 2: 1}
print(i, nums, distinct_numbers,i-k , nums[i-k])
2 [1, 2, 3, 2, 2, 1, 3] {'count': 3, 1: 1, 2: 1, 3: 1} 0 1
3 [3, 2, 3, 2, 2, 1, 3] {'count': 2, 2: 2, 3: 1} 1 2
4 [3, 2, 3, 2, 2, 1, 3] {'count': 2, 2: 2, 3: 1} 2 3
5 [3, 2, 2, 2, 2, 1, 3] {'count': 2, 2: 2, 1: 1} 3 2
6 [3, 2, 2, 2, 2, 1, 3] {'count': 3, 2: 1, 1: 1, 3: 1} 4 2
output: [3, 2, 2, 2, 3]


Press Enter to exit terminal

"""


def unique_numbser_count(distinct_numbers, key):
    if key not in distinct_numbers:
        distinct_numbers[key] = 1
        distinct_numbers['count'] +=1
    else:
        distinct_numbers[key] +=1


def distinct_numbers_in_each_subarray(nums, k):
    k = k-1
    distinct_numbers = {}
    distinct_numbers['count'] = 0
    for i in range(k):
        unique_numbser_count(distinct_numbers, nums[i])
        
    if len(nums) < k+1:
        return distinct_numbers['count']
    print('distinct_numbers', distinct_numbers)
    for i in range(k, len(nums)):
        
        unique_numbser_count(distinct_numbers,  nums[i])
        print(i, nums, distinct_numbers,i-k , nums[i-k])
        cur_count = distinct_numbers['count']
        if nums[i-k] in distinct_numbers:
            distinct_numbers[nums[i-k]] -=1
            
            if distinct_numbers[nums[i-k]] ==0:
                del distinct_numbers[nums[i-k]]
                distinct_numbers['count'] -=1
                
        nums[i-k] =cur_count
        

    return nums[:len(nums)-k]
    
print(distinct_numbers_in_each_subarray([1,2,3,2,2,1,3],  3))
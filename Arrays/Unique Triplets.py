""" 
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]

"""
def sum_of_tripltes():

def Unique_Triplets():
    all_triplets = []
    for i in given_array:
        first_ele = [i]
        rest_elements = []
        for j in given_array:
            if i==j:
                continue
            rest_elements.append(j)
            if len(rest_elements)==2:
                cur_triplet = first_ele+rest_elements
                if sum(cur_triplet) ==0:
                    all_triplets.append(cur_triplet)


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

"""

Input: nums = [2.1,5,3], target = 4
Output: [1, 3]
Explanation: Because nums[1] + nums[3] == 4, we return [1, 3].


Check every combination of two values and see if they can sum up to our target in this case target is 4

Start at index 0 and we scan through the remainder of the array and check if any of those numbers added 2 sums to our target 4

index 1 is 1 scan through the remainder of the array and check again if any of those numbers added 1 sums up to our target 4 

NOTICE : we didn't have to check the values that came before 1 because we already checked the combination 2 and 1 when we checked every combination with 2


We are looking for 4 - 1 which is 3, so this is the only value that will equal the target -- so checking if value 3 exists

"""

"""
Using a Hash Map : mapping each value to the index of each value 
Val : index
 2  :   0
 1  :   1  <---- 4-3 exists and it's index is 1 ( 4 - 1 = 3)
 5  :   2
index   0   1    2      3
        [2,  1,   5,     3]
        4-2  4-1  4-5   4-3
        2    3    -1    1    
        
        
output: [1, 3]

Time Complexity: O (n)
Memory Complexity: O (n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return        
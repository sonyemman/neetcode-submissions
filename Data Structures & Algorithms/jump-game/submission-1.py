'''
greedy approach
    - start with a goal at the last index 
    - iterate from len(nums) - 1 to beginning of array 
        - if i + nums[i] >= goal
        - set goal = i 
    - if goal == 0 then return true and if not return false 
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 

        for i in range(len(nums) - 2, -1, -1): 
            if nums[i] + i >= goal: 
                goal = i 
        
        return goal == 0 

    

    
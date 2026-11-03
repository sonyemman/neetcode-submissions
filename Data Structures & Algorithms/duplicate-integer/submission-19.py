"""
solution:
- add a number to a set and if it cant be added then it is falase 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = {} 

        for idx, num in enumerate(nums): 
            if num in li and idx != li[num]: 
                return True 

            li[num] = idx 
        
        return False 
        
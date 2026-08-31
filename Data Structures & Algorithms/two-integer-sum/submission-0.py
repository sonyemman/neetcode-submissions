class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i, num in enumerate(nums): 
            complement = target - num
            if complement in hMap: 
                return [hMap[complement], i]
            hMap[num] = i
        
        return [-1, -1]
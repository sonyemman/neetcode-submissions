class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, currSum = nums[0], 0

        for num in nums: 
            currSum += num 
            res = max(res, currSum)
            currSum = max(currSum, 0)
            

        return res

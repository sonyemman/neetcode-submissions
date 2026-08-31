class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] #max of an array of [1] is 1  
        curr = 0 

        for num in nums: 
            curr = curr + num # running sum 
            maxSum = max(maxSum, curr)
            curr = max(curr, 0)

        return maxSum

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set() 
        sorted(nums)

        for num in nums:
            if num in hset:
                return True 
            hset.add(num)

        return False
         
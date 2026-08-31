# nums = [-1,0,1,2,-1,-4]
#edge cases: 1) first element is positive 2) 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        for i, num in enumerate(nums): 
            if num > 0: 
                break 

            #duplicates 
            if i > 0 and num == nums[i - 1]: 
                continue 
             
            l, r = i + 1, len(nums) - 1

            while l < r : 
                _sum = nums[i] + nums[l] + nums[r]

                if _sum > 0: 
                    r -= 1 
                elif _sum < 0: 
                    l += 1 
                else: 
                    res.append([num, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    #skip duplicates 
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1 

        return res
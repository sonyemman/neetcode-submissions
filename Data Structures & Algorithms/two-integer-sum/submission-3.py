'''
nums = [3,4,5,6] target = 7 
{
4:0,
3:1,
2:2,
1:3
}
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
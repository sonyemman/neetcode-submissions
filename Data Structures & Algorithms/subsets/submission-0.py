class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(i, comb): 
            if i == len(nums):
                res.append(comb.copy())
                return 

            
            comb.append(nums[i])
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)

            return comb
        dfs(0, [])
        return res

        
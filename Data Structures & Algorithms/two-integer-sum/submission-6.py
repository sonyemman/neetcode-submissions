"""
1. make a hashmap 
2. store the number as a key and index as the value because we want to have the indexes of the additive numbers 
3. loop through the array, add to the dic 
4. at a specific index and number, calculate if the othe rnumber is in the hashmap (complement) 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} 

        for i, num in enumerate(nums): 
            complement = target - num
            if complement in hmap: 
                return [hmap[complement], i]

            hmap[num] = i

        return []

        
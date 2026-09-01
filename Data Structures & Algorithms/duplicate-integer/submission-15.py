
# [3,4,5,6]
# [0,0,0,0,0,0,0,0]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_size = len(nums) * 2 
        hash_array = [None] * hash_size
        for num in nums: 
            index = num % hash_size 

            while hash_array[index] is not None:

                if hash_array[index] == num: 
                    return True 

                index = (index + 1) % hash_size 

            hash_array[index] = num
         

        
        return False


        
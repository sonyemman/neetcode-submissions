class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0 

        for num in nums: 
            #check if num is start of the sequence 
            if (num - 1) not in numsSet:
                length = 0 
                while (num + length) in numsSet: 
                    length += 1
                longest = max(length, longest)
        return longest 
        

            #if it is, check if it has a number to the right in the set
                #if so, increment counter 

            #when you get to the end of the sequence - save to longest 
            #reset counter before going on to next num 
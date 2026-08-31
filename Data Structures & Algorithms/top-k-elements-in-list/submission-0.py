from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #iterate and bucket sort nums into a dict {1:1 , 2:2: 3:3}
        # sort dict by frequency 
        # iterate again through the dict k times and add the key into the res 

        res = [] 
        freqDict = defaultdict(int)
        #bucket sort 
        for num in nums:
            freqDict[num] += 1
        
        #save this: sorting contents of a dict 
        sorted_dict = sorted(freqDict.items(), key=lambda item: item[1])

        while len(res) < k: 
            res.append(sorted_dict.pop()[0])

        return res
        
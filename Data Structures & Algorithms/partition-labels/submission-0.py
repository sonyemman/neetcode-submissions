from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = end = 0 
        res, hmap = [], defaultdict(int)

        for i, char in enumerate(s):
            hmap[char] = i
        
        for i in range(len(s)):
            size += 1
            end = max(end, hmap[s[i]])

            if end == i: 
                res.append(size)
                size = 0
            
        
        return res
        
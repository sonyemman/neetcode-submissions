# bucket sort 
# time O(m * n) space O(m)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs: 
            #constant time iteration 
            count = [0] * 26 
            for char in string: 
                count[ord(char) - ord('a')] +=  1 #convert 'a' to 1 
            
            # using char -> char freq to be hash key 
            res[tuple(count)].append(string)

        return list(res.values())
        
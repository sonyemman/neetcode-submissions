# strs = ["act","pots","tops","cat","stop","hat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            count = 26 * [0]
            for c in string: 
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(string)
        return list(anagrams.values())

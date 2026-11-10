class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums: 
            freq[num] += 1
        
        arr = [] 
        for num, count in freq.items(): 
            arr.append([count, num])
        
        arr.sort() # cost would be here (logN)
        res = [] 
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res




        
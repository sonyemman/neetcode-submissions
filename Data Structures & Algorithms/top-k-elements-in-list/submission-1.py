'''
heap solution 
1. create default dict 
2. push to heap {freq: num} 
3. pop when heap is greater than k 
4. pop k times into the res array 
'''
from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        res = [] 
        heap = []

        for num in nums: 
            count[num] += 1 
        
        for num in count.keys(): 
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        for i in range(k): 
            res.append(heapq.heappop(heap)[1])

        print(count.items())
        print(res)

        return res


        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            #process stones 
            heaviestStone = heapq.heappop(stones)
            heaviestStone2 = heapq.heappop(stones)

            if heaviestStone2 > heaviestStone: 
                diff = heaviestStone - heaviestStone2
                heapq.heappush(stones, diff)

            
        stones.append(0)
        return abs(stones[0]) if len(stones) > 0 else 0
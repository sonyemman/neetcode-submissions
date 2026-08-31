class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # make negative 
        heapq.heapify(stones) 


        while len(stones) > 1:
            #pop twice 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones) 

            if x < y: 
                heapq.heappush(stones, x - y)
            print(stones)
        stones.append(0)
        return abs(stones[0])
       

            
        
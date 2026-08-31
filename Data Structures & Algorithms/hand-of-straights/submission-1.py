'''
hand = [1,2,4,2,3,5,3,4], groupSize = 4
'''
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False 
        
        freqMap = Counter(hand)
        minH = list(freqMap.keys())
        heapq.heapify(minH)
        
        while minH:
            #peek and find the min element 
            first = minH[0]
            for i in range(first, first + groupSize): 
                #check if element is in freqMap and if not then cant find consecutive number
                if i not in freqMap: 
                    return False
                freqMap[i] -= 1
                if freqMap[i] == 0: 
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True                
        
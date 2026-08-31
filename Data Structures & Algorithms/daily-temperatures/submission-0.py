# [30,38,30,36,35,40,28]
# [30, ]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, index
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures): 
            while stack and stack[-1][0] < temp:
                temperature, idx = stack.pop() 
                res[idx] = i - idx 
            stack.append((temp, i))
        return res 
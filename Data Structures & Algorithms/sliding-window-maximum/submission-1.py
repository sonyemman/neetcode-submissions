class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() 
        res = [] 

        for i, num in enumerate(nums): 
          # purge nums with index not in window 
          while queue and queue[0] < i - k + 1:
            queue.popleft()

          while queue and num > nums[queue[-1]]: 
            queue.pop()

          queue.append(i)

          if i >= k - 1: 
            res.append(nums[queue[0]])


        return res 
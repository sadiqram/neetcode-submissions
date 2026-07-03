from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:    
                tracker[num] +=1
        
        pq = PriorityQueue()

        for key,val in tracker.items():
            pq.put((-val,key))

        n = k
        res = []
        while n > 0:
            res.append(pq.get()[1])
            n-=1
        return res
        
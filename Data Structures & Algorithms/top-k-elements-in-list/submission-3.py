from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
    
        for num in nums:
            if num in lookup:
                lookup[num]+=1
            else:
                lookup[num] = 1
            
        pq = PriorityQueue()

        for key,v in lookup.items():
            pq.put((-v,key))
        
        res = []
        i = 0
        while i < k:
            res.append(pq.get()[1])
            i+=1

        return res
        
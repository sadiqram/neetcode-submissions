from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        pq = PriorityQueue()

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num]+=1
        for key,v in freq.items():
            pq.put((-v,key))

        i = 0
        res = []
        while i < k:
            res.append(pq.get()[1])
            i+=1
        return res
            

            

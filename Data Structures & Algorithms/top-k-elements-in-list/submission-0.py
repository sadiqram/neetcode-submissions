from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

    
        ret = []
        tracker = {num: 0 for num in nums}
        for num in nums:
            tracker[num] +=1
    
    
        pq = PriorityQueue()
        for num, count in tracker.items():
            pq.put((-count,num))

        n = k

        while n >0:
            ret.append(pq.get()[1])
            n-=1
        return ret
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Improvise code
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1: #need to think if there is only 1 element
            x = - heapq.heappop(maxHeap)
            y = - heapq.heappop(maxHeap)
            res = x - y
            if x != y:
                heapq.heappush(maxHeap, - (x - y))
        return  - maxHeap[0] if maxHeap else 0     


        # maxHeap = []
        # for s in stones:
        #     maxHeap.append(-s)

        # heapq.heapify(maxHeap)
        # while maxHeap:
        #     x = heapq.heappop(maxHeap)
        #     y = heapq.heappop(maxHeap)

        #     res = y - x
        #     if res > 0:
        #         heapq.heappush(maxHeap, res)

        # return res            
        
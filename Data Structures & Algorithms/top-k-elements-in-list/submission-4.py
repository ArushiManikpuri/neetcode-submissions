class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_element = {}
        for num in nums:
            freq_element[num] = freq_element.get(num, 0) + 1

        min_heap = []

        for num, freq in freq_element.items():
            heapq.heappush(min_heap, (freq, num))
        
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]

        
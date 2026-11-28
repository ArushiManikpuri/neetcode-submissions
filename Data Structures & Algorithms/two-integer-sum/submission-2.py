class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} #hashmap

        for i,n in enumerate(nums):
            num = target - n
            if num in preMap:
                return ([preMap[num],i])
            preMap[n] = i
        

        

        
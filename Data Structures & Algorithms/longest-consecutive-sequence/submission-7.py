class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1
            
                while cur_num + 1 in num_set:
                    cur_length += 1
                    cur_num += 1
                max_length = max(cur_length, max_length)
        return max_length
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #keep all unique element
        max_length = 0

        for num in nums:
            if num - 1 not in num_set:
                current_length = 1
                current_num = num #means num_set number will be starting from this number

                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1

           #The time it found current_num now no more in set.
                max_length = max(current_length, max_length)
        return max_length         


        
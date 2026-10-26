class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_length = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                current_num = num
                current_length = 1
            # 2
                while current_num + 1 in hash_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)    
            
        
        return max_length



        


        
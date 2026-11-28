class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_result = [1] * n
        right_result = [1] * n

        left_prod = 1
        for i in range(n):
            left_result[i] *= left_prod
            left_prod *= nums[i]

        right_prod = 1
        for i in range(n - 1, -1, -1):
            right_result[i] *= right_prod
            right_prod *= nums[i]
        
        return [left_result[i] * right_result[i] for i in range(n)]



        
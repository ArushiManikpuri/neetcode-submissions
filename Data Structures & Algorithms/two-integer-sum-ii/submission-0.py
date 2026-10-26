class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointer approach

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            if total > target:
                right -= 1

            if total < target:
                left += 1
        return [-1, -1]                
        
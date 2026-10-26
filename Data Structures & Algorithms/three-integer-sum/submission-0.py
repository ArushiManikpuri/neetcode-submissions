class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        #3 pointer approach
        n = len(nums)
        result = []
        for i in range(n -2):
            #skip duplicate while starting
            if i > 0 and nums[i -1] == nums[i]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    #skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    #skip duplicates    
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1

                    left += 1
                    right -= 1    

                elif sum < 0:
                    left += 1

                else:
                    right -= 1
        return result                            

        
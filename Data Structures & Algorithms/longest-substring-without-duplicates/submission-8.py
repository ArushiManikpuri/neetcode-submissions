class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            if s[right] not in result:
                result.add(s[right])
                right += 1
            
            else:
                result.remove(s[left])
                left += 1

            max_length = max(max_length, len(result))
            
        return max_length

            


        
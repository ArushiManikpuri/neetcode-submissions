class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        unique_char = set()
        maxlength = 0
        if len(s) == 0:
            return 0
        while right < len(s):
            if s[right] not in unique_char:
                unique_char.add(s[right])
                maxlength = max(maxlength, right - left + 1)
                right += 1

            else:
                unique_char.remove(s[left])
                left += 1
        return maxlength
            


        
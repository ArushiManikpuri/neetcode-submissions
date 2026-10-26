class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left, right = 0, 0
        unique_charset = set()

        while right < len(s):
            if s[right] not in unique_charset:
                unique_charset.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                unique_charset.remove(s[left])
                left += 1

        return max_length        





        
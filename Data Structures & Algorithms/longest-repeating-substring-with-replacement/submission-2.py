class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_freq = 0
        cur_freq = {}
        maxlength = 0
        while right < len(s):
            cur_freq[s[right]] = cur_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, cur_freq[s[right]])

            if (right - left + 1) - max_freq > k:
                cur_freq[s[left]] -= 1
                left += 1
            
            maxlength = max(maxlength, right - left + 1)
            right += 1
        return maxlength
        

        
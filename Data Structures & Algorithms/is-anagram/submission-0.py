class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for ch in t:
            if ch not in char_freq or char_freq[ch] == 0:
                return False

            char_freq[ch] -= 1
        return True                
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_frequency = {}
        for char in s:
            char_frequency[char] = 1 + char_frequency.get(char, 0)
        
        for ch in t:
            if ch not in char_frequency or char_frequency[ch] == 0:
                return False
            char_frequency[ch] -= 1
            
        return True
        
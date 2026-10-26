class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency = {}

        if len(s) != len(t):
            return False

        for char in s:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        #comparing with other string
        for char in t:
            if char not in char_frequency or char_frequency[char] == 0:
                return False
            char_frequency[char] -= 1
        return True

        
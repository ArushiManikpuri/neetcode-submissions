class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_char = {}
        for char in s1:
            freq_char[char] = freq_char.get(char,0) + 1
        
        freq_temp_char = {}
        left = 0
        right = 0

        while right < len(s2):   
            freq_temp_char[s2[right]] = freq_temp_char.get(s2[right], 0) + 1
            
            #window check
            if right - left + 1 == len(s1):
                if freq_char == freq_temp_char:
                   return True

                freq_temp_char[s2[left]] -= 1
                if freq_temp_char[s2[left]] == 0:
                    del freq_temp_char[s2[left]]
                left += 1                
            
            right += 1

        return False


        
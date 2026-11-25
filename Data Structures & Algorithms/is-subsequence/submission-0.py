class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        #2 pointer j traverse t
        #i traverse s and check if there's match
        i,j = 0,0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
            
        return i == len(s)

        
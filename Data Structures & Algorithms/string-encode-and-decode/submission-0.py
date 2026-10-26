class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded    


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i) # index 1
            size = int(s[i:delimiter])
            start_pos = delimiter + 1 #2

            end_pos = start_pos + size
            decoded.append(s[start_pos:end_pos]) #-->####   5#Hello
            i = end_pos
        return decoded    



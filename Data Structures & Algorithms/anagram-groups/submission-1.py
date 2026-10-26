class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = {}
        for s in strs:
            word = "".join(sorted(s))
            if word in sorted_word:
                sorted_word[word].append(s)
            else:
                sorted_word[word] = [s]
        return list(sorted_word.values())
        
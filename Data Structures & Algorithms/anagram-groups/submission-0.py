class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)  
        for s in strs:
            alpha_list  = [0]*26
            for c in s:
                alpha_index  = ord(c) - ord('a')
                alpha_list[alpha_index] += 1
            anagram[tuple(alpha_list)].append(s)
        return list(anagram.values())
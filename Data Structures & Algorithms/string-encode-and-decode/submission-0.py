class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" +s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = []
        i = 0
        while i < len(s):
            j = i
            while   s[j] != '#':
                j += 1
         
            length = int(s[i:j])
            result.append(s[j+1:j+length+1])
            i = j + length + 1

        return result



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict_s = {}
        char_dict_t = {}
        
        for x in s:
            if char_dict_s.get(x) is None:
                char_dict_s[x] = 1
            else:
                char_dict_s[x] = char_dict_s[x] + 1 
        for x in t:
            if char_dict_t.get(x) is None:
                char_dict_t[x] = 1
            else:
                char_dict_t[x] = char_dict_t[x] + 1 
        
        if len(char_dict_s) != len(char_dict_t):
            return False
        else:
            for key in char_dict_s:
                if (key not in char_dict_t)  or (char_dict_s[key] != char_dict_t[key]):
                    return False
        return True
        

        
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        str_len = len(s)
        if str_len % 2  == 1 :
            return False
        paranthisis_pair = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        } 
        stack  = deque()
        
        for ch in s:
            if ch in paranthisis_pair.keys():
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                ele = stack.pop()
                if ch != paranthisis_pair[ele]:
                    return False
        return False if len(stack) >0 else True



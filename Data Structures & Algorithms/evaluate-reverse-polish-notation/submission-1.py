class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = {'+', '-', '*', '/'}
        for c in tokens:
            if c not in operators:
                stk.append(int(c))
            else:
                op1 = stk.pop()
                op2 = stk.pop()
                if c == '+':
                    stk.append(op2 + op1)
                elif c == '-':
                    stk.append(op2 - op1)
                elif c == '*':
                    stk.append(op2 * op1)
                elif c == '/':
                    stk.append(int(op2 / op1))
        return stk[-1]
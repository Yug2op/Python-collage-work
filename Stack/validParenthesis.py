class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if ch == '('or ch == '{' or ch == '[':
                stk.append(ch)
            elif ch == ')':
                if (len(stk) != 0) and (stk[-1] == '('):
                    stk.pop()
                else:
                    return False
            elif ch == '}':
                if (len(stk) != 0) and (stk[-1] == '{'):
                    stk.pop()
                else:
                    return False
            else:
                if (len(stk) != 0) and (stk[-1] == '['):
                    stk.pop()
                else:
                    return False
        return len(stk) == 0 
        
soln = Solution()
print(soln.isValid("({[]})()"))
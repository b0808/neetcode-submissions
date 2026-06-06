class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        k = {'[':']','{':'}','(':')'}
        for i in range(len(s)):
            if s[i] in k:
                stack.append(s[i])
            else:
                if stack==[]:
                    return False
                elif s[i] == k[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        
        return stack==[]
            



                    
        
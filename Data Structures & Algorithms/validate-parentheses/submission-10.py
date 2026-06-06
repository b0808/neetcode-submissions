class Solution:
    def isValid(self, s: str) -> bool:
        j = []
        k = {'[':']','{':'}','(':')'}
        for i in range(len(s)):
            if s[i] in k:
                j.append(s[i])
            else:
                if j==[]:
                    return False
                elif s[i] == k[j[-1]]:
                    j.pop(-1)
                else:
                    return False
        
        return j==[]
            



                    
        
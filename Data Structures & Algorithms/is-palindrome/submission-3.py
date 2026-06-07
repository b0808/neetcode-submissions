class Solution:
    def isPalindrome(self, s: str) -> bool:

        k = len(s)

        start = 0
        second = k-1

        while second>start:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[second].isalnum():
                second-=1
                continue
            if s[start].lower()!=s[second].lower():
                return False
            else:
                start+=1
                second-=1
        return True






        
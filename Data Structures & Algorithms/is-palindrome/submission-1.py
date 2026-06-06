class Solution:
    def isPalindrome(self, s: str) -> bool:
        news =str()
        for c in s:
            if c.isalnum():
                news = news + c.lower()
        return news == news[::-1]


        
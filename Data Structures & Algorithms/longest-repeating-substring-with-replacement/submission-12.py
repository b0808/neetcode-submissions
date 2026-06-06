class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxv = 0
        l = 0 
        r = 1
        d = {}
        #s="AABABBA"

        d[s[l]] = 1
        while r<len(s):
            if s[r] in d:
                d[s[r]] = d[s[r]]+1
            else:
                d[s[r]] = 1
            print(d)
            max_key = max(d, key=d.get)
            max_value = d[max_key]
            if r-l+1 - max_value <= k:
                maxv = max(maxv,r-l+1)
                print(r-l+1, max_value)
                r =r+1
            else:
                d[s[l]] = d[s[l]] - 1
                d[s[r]] = d[s[r]] - 1
                l = l+1
                

        return maxv



        
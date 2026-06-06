class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        maxv = 1
        d = {}
        if len(s)>0:
            d[s[l]] = 0
            while r<len(s):
                print(l,r)
                if s[r] in d:
                    if l<=d[s[r]]:
                        l = d[s[r]]+1
                        d[s[r]] = r
                        r= r+1
                    else:

                        d[s[r]] = r
                        maxv = max(r-l+1,maxv)
                        # print(maxv)
                        r = r+1


                
                else:
                    d[s[r]] = r
                    maxv = max(r-l+1,maxv)
                    r = r+1
        else:
            return 0
            print(d)
        return maxv
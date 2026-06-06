class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxv = 0
        for i in range(len(s)):
            new = s[i]
            d={}
            d[s[i]] = 1
            for j in range(i+1,len(s)):
                if s[j] in d:
                    d[s[j]] = d[s[j]]+1
                else:
                    d[s[j]] = 1
                max_key = max(d, key=d.get)
                max_value = d[max_key]
                if j-i+1 - max_value <= k :
                    maxv = max(maxv,j-i+1)
                new = new +s[j]
        return maxv



        
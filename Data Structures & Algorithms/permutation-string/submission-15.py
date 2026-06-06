class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z')+1)], 0)
        d2 = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z')+1)], 0)
        r =0
        for i in range(len(s1)):
                d[s1[i]] = d[s1[i]]+1
                d2[s2[i]] = d2[s2[i]]+1
        while r<len(s2)-len(s1):
            if d!=d2:
                d2[s2[r]] = d2[s2[r]] -1 
                d2[s2[r+len(s1)]] = d2[s2[r+len(s1)]] +1
                r = r+1
                # print(d,d2)

            else:
                return True

                
        return d == d2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # initialize dicts a–z with 0
        d = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z')+1)], 0)
        d2 = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z')+1)], 0)

        r = 0

        # fill counts for s1 and first window of s2
        for i in range(len(s1)):
            d[s1[i]] += 1
            d2[s2[i]] += 1

        # sliding window
        while r < len(s2) - len(s1):
            if d == d2:
                return True
            d2[s2[r]] -= 1
            d2[s2[r + len(s1)]] += 1
            r += 1

        # final check for the last window
        return d == d2

                
        return max(d.values())==0
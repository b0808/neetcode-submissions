class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxv = 0
        l = 0
        d = {}

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            max_value = max(d.values())

            if (r - l + 1) - max_value > k:
                d[s[l]] -= 1
                l += 1

            maxv = max(maxv, r - l + 1)

        return maxv



        
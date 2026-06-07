class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0
        m = 0
        k = 0
        d = set()
        while j<len(s):
            if s[j] not in d:
                d.add(s[j])
                k = k+1
                j = j+1
                m = max(m, k)
            else:
                d.remove(s[i])
                i = i+1
                k = k-1
        return m

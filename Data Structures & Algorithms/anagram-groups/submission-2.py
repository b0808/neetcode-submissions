class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dic = defaultdict(list) #s:m*n
        # for k in strs: # t:m
        #     m = ''.join(sorted(k)) #t: nlogn
        #     print(m)
        #     dic[m].append(k)
        #     print(dic)
        # return list(dic.values())

        dic = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            dic[tuple(count)].append(s)
        return list(dic.values())



        
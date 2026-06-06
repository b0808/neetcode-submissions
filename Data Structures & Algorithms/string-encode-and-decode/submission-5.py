class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        str = ""
        for k in strs:
            str = str + k + "`"
        print(str)
        return str

    def decode(self, s: str) -> List[str]:
        print(s)
        k =[]
        b=""
        for i in range(len(s)):
            if s[i]=="`":
                k.append(b)
                b=""
            else:
                b = b+s[i]

        return k
            


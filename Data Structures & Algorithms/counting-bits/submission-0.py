class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for m in range(n+1):

            k =0
            for i in range(32):
                if m&1 !=0:
                    k = k+1
                m = m>>1
            out.append(k)
        return out
            

        
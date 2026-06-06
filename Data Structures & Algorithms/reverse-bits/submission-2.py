class Solution:
    def reverseBits(self, n: int) -> int:
        k = 0
        for i in range(32):
            if n&1 ==1:
                k = k|(1<<(31-i))
            if n ==0:
                break
            n = n>>1
        return k


        
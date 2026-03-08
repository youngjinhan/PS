class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        cand = [i for i in range(2**n)]
        nums_10 = [int(i, 2) for i in nums]

        cand_bi = [format(c, '0' + str(n) +'b') for c in cand if c not in nums_10]

        return cand_bi[0]
        
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(0, n - 2*k + 1):
            flag = True
            for j in range(k-1):
                if nums[i+j] >= nums[i+j+1] or nums[i+k+j] >= nums[i+k+j+1]:
                    flag = False
                    break
            if flag:
                return True

        return False
            
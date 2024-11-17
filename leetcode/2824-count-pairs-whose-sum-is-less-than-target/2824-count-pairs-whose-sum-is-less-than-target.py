class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        left, right = 0, n-1
        for i in range(n-1):
            while i < right and nums[i] + nums[right] >= target:
                right -= 1
            if i >= right:
                break
            ans += right - i
        return ans
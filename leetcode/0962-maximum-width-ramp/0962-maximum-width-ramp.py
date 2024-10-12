class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        part_max_list = [nums[n-1]] * n
        
        for i in range(n-2, -1, -1):
            part_max_list[i] = max(nums[i], part_max_list[i+1])

        left, right, ans = 0, 0, -1
        while right < n:
            while left < right and nums[left] > part_max_list[right]:
                left += 1
            ans = max(ans, right-left)
            right += 1

        return ans
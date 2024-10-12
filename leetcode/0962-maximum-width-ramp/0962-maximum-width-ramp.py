class Solution(object):
    def maxWidthRamp(self, nums):
        '''
        Monotonic Decreasing Stack
        '''
        indices_stack = []
        n = len(nums)
        ans = 0
        for i in range(n):
            if not indices_stack or nums[indices_stack[-1]] >= nums[i]:
                indices_stack.append(i)
        
        for j in range(n-1, -1, -1):
            if not indices_stack:
                    break
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                ans = max(ans, j-indices_stack[-1])
                indices_stack.pop()
        return ans

        '''
        Two Pointers
        Time Complexity : O(n)
        '''
        n = len(nums)
        part_max_list = [nums[n-1]] * n
        
        for i in range(n-2, -1, -1):
            part_max_list[i] = max(nums[i], part_max_list[i+1])

        left, right, ans = 0, 0, 0
        while right < n:
            while left < right and nums[left] > part_max_list[right]:
                left += 1
            ans = max(ans, right-left)
            right += 1

        return ans
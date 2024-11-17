class Solution:
    def lower_bound(self, nums, low, high, element):
        '''
        Binary Search Solution
        Time Limit Exceeded
        '''
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # Assume we have picked nums[i] as the first pair element.

            # `low` indicates the number of possible pairs with sum < lower.
            low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])

            # `high` indicates the number of possible pairs with sum <= upper.
            high = self.lower_bound(
                nums, i + 1, len(nums) - 1, upper - nums[i] + 1
            )

            # Their difference gives the number of elements with sum in the
            # given range.
            ans += high - low

        return ans

    '''
    My Solution.. 
    Time Limit Exceeded
    '''
    '''
        nums.sort()
        n = len(nums)
        ans = 0
        left, right = 0, n-1

        for i in range(n-1):
            while i < right and nums[i] + nums[right] > upper:
                right -= 1
            if i >= right:
                break
            tmp = right
            while i < tmp and nums[i] + nums[tmp] >= lower:
                ans += 1
                tmp -= 1
        return ans
    '''
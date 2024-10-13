class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 직접 풀지 못한 문제
        # 해답 참고
        n = len(nums)
        indices = [i for i in range(n)]

        # Sort indices based on corresponding values in nums and ensure stability
        indices.sort(key=lambda i: (nums[i], i))

        min_index = n  # Minimum index encountered so far
        max_width = 0

        # Calculate maximum width ramp
        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width
        


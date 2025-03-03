class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, mid, right = [], [], []
        for num in nums:
            if num == pivot:
                mid.append(num)
            elif num > pivot:
                right.append(num)
            else:
                left.append(num)
        return left + mid + right
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx_dic = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in val_idx_dic:
                return [i, val_idx_dic[complement]]
            val_idx_dic[nums[i]] = i

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_idx_dic = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in val_idx_dic:
                return [i, val_idx_dic[complement]]
            val_idx_dic[nums[i]] = i
                   
            
        
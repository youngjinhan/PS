class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> valIdxMap = new HashMap<>();
        for (int i =0; i< nums.length; i++) {
            int complement = target - nums[i];
            if (valIdxMap.containsKey(complement)) {
                return new int[]{i, valIdxMap.get(complement)};
            }
            valIdxMap.put(nums[i], i);
        }
        return new int[]{};
    }
}
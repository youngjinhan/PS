class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> ans = new ArrayList<>();
        int val = -1;
        for (int i = 0; i < groups.length; i++) {
            if (val != groups[i]) {
                ans.add(words[i]);
                val = groups[i];
            }
        }
        return ans;
    }
}
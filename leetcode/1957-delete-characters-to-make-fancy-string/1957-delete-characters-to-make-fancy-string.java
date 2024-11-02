class Solution {
    public String makeFancyString(String s) {
        int n = s.length();
        char prev = s.charAt(0);
        int freq = 1;
        StringBuffer ans = new StringBuffer();
        ans.append(prev);

        for (int i =1; i<n; i++) {
            if (s.charAt(i) == prev) freq++;
            else {
                prev = s.charAt(i);
                freq = 1;
            }
            if (freq < 3) ans.append(prev);
        }
        return ans.toString();
    }
}
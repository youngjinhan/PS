class Solution {
    public int minSwaps(String s) {
        int cnt = 0;
        for (char c : s.toCharArray()) {
            if (c == '[') cnt++;
            else if (cnt > 0) cnt--;
        }
        return (cnt + 1) / 2;
    }
}
class Solution {
    public int minLength(String s) {
        int cur = 0;
        char[] result = new char[s.length()];
        for (char c : s.toCharArray()) {
            if (cur > 0 && ((result[cur-1] == 'A' && c == 'B') || (result[cur-1] == 'C' && c == 'D'))) cur--;
            else {
                result[cur++] = c;
            }
        }
        return cur;
    }
}
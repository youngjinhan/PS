class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ans = new ArrayList<>();
        int cur = 1, cnt = 1; 
        ans.add(cur);

        // 10009 1001 10010 ... 10019 .. 10025 ... 18999 
        while (cnt < n) {
            if (cur * 10 <= n) {
                cur *= 10;
            } else {
                while (cur % 10 == 9 || cur >= n) {
                    cur /= 10;
                }
                cur++;
            }
            ans.add(cur);
            cnt++;
        }

        return ans;
    }
}
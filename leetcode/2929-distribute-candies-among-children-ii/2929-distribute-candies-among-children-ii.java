class Solution {
    public long distributeCandies(int n, int limit) {
        long ans = 0L;

        for (int i = 0; i <= Math.min(n, limit); i++) {
            if (n - i > limit * 2) continue;
            ans += Math.min(limit, n-i) - Math.max(0, n-i-limit) + 1;
        }

        return ans;
    }
}
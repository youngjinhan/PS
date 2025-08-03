class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        // 6*4 + 9*3 - 3*2 
        // [-3, 3], [0, 9]

        int ans = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1);

        if (Math.min(ax2, bx2) <= Math.max(ax1, bx1) || Math.min(ay2, by2) <= Math.max(ay1, by1)) {
            return ans;
        }
        ans -= (Math.min(ax2, bx2) - Math.max(ax1, bx1)) * (Math.min(ay2, by2) - Math.max(ay1, by1));
        return ans;
    }
}
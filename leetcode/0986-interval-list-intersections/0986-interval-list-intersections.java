class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> ans = new ArrayList<>();
        int m = firstList.length, n = secondList.length;
        int x = 0, y = 0;

        while (x < m && y < n) {
            int xstart = firstList[x][0], xend = firstList[x][1];
            int ystart = secondList[y][0], yend = secondList[y][1];

            if (xstart > yend) {
                y++;   
            } else if (ystart > xend) {
                x++;
            } else {
                int start = Math.max(xstart, ystart);
                int end = Math.min(xend, yend);

                ans.add(new int[]{start, end});
                if (xend > yend) y++;
                else if (xend == yend) {
                    x++;
                    y++;
                } else x++;
            }
        }

        int[][] answer = new int[ans.size()][2];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        return answer;
    }
}
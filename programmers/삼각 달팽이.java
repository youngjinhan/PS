class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n*(n+1)/2];
        var field = new int[n][n];
        
        int x = -1, y = 0, cnt = 1;
        
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) {
                    x++;
                } else if (i % 3 == 1) {
                    y++;
                } else {
                    x--;
                    y--;
                }
                field[x][y] = cnt++;
            }
        }
        
        cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j<n; j++) {
                if (field[i][j] == 0) break;
                answer[cnt++] = field[i][j];
            }
        }
        return answer;
    }
}

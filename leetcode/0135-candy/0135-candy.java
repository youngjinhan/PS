class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        int cnt = 0;
        Arrays.fill(candies, 1);
        for (int i = 0; i< n - 1; i++) {
            if (ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]) {
                candies[i] = candies[i+1] + 1;
            } else if (ratings[i] < ratings[i+1] && candies[i] >= candies[i+1]) {
                candies[i+1] = candies[i] + 1;
            }
        }

        for (int i = n - 1; i > 0; i--) {
            if (ratings[i] > ratings[i-1] && candies[i] <= candies[i-1]) {
                candies[i] = candies[i-1] + 1;
            } else if (ratings[i] < ratings[i-1] && candies[i] >= candies[i-1]) {
                candies[i-1] = candies[i] + 1;
            }
            cnt += candies[i];
        }

        return cnt + candies[0];
    }
}
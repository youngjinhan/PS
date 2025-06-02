class Solution {

    /**
            Solution 2. 수학적 풀이
            사탕 n개를 3개로 나누는 것은 사탕 n개와 2개의 막대기를 나열하는 방법과 같다.
            따라서 n+2 C 2 와 같다.

            이때 각 구역의 사탕이 limit개를 초과하면 안되므로 이 경우를 제외해야 한다.
            그 경우는 3곳 중 한 곳을 골라 limit + 1 개의 사탕을 미리 배정해주고 나머지 개수를 3 곳으로 나누는 방법과 같다.
            따라서 3곳 중 하나 정하고 거기에 (n - (limit+1) + 2) 개 중에서 2개를 고르는 방법과 같다.
            식으로 하면 3 * (n - (limit+1) + 2) C 2 와 같다.

            이때 만약 두 곳이 limit 개를 초과한다면 위의 한 곳이 초과하는 경우에서 중복 제거했으므로 더해줘야 한다.
            마찬가지로 세 곳이 limit 개를 초과한다면 두 곳이 초과하는 경우에 중복 추가했으므로 빼줘야 한다.

     */
    public long distributeCandies(int n, int limit) {
        return cal(n+2) - 3 * cal(n - (limit + 1) + 2) + 3 * cal(n - 2 * (limit + 1) + 2) - cal (n - 3 * (limit + 1) + 2);
    }

    private long cal(int x) {
        if (x < 0) return 0;
        return (long) x * (x-1) / 2;
    }

    // /**
    //         Solution 1. Enumeration
    //         첫번째 아이가 i 만큼 가져가면, 두번째와 세번째 아이는 n-i 를 나눠 가져야 한다.
    //         i의 범위는 0개부터 limit 까지인데, n이 limit보다 작을 수도 있으므로 n과 limit 중 작은 숫자까지 가져갈 수 있다.
    //         두번째 아이가 j 만큼 가져가면 세번째 아이는 자동적으로 n-i-j만큼 가져가는 것이므로, 두번째 아이가 가져갈 수 있는 범위를 정하면 된다.

    //         n-i <= limit 라면, 두번째 아이는 최소 0개를 가져가도 된다.
    //         limit < n-i <= 2 * limit 라면, 최소 n-i-limit 개 만큼은 가져가야 세번째 아이가 limit개를 가져감으로써 모든 사탕을 가져갈 수 있다. 이것보다 더 적게 가져가면 세번째 아이가 limit개를 가져가도 남는 사탕이 존재한다.
    //         n-i의 개수가 2 * limit 보다 크면 어떻게 해도 남은 아이들이 사탕을 다 가져갈 수 없다.

    //         이제 두번째 아이가 최대로 가져갈 수 있는 숫자를 살펴보자.
    //         n-i <= limit이라면 n-1만큼 다 가져갈 수 있다. 
    //         limit < n-i <= 2 * limit이라면 최대 limit만큼 가져갈 수 있다.
    //         n-i > 2 * limit이라면 어떻게해도 불가능하다.

    //         따라서 범위를 계산해보면 max(0, n-i-limit) <= j <= min(n-i, limit) 이다.
    // */
    // public long distributeCandies(int n, int limit) {
    //     long ans = 0L;

    //     for (int i = 0; i <= Math.min(n, limit); i++) {
    //         if (n - i > limit * 2) continue;
    //         ans += Math.min(limit, n-i) - Math.max(0, n-i-limit) + 1;
    //     }

    //     return ans;
    // }
}
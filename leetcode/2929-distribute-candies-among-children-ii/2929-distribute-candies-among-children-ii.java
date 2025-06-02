class Solution {
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
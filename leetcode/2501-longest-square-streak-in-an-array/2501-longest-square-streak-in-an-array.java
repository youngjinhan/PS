class Solution {
    public int longestSquareStreak(int[] nums) {
        final int MAX_NUM = 100000;
        Set<Long> numSet = new HashSet<>();
        for (long num: nums) {
            numSet.add(num);
        }

        List<Long> numList = new ArrayList<>(numSet);
        Collections.sort(numList);

        Map<Long, Integer> squareCountMap = new HashMap<>();

        for (Long num: numList) {
            squareCountMap.put(num, 1);
        }

        int best = 0;

        for (Long num: numList) {
            int streak = 1;
            for (long i = num * num; i <= MAX_NUM; i *= i) {
                if (squareCountMap.get(i) == null) {
                    break;
                }
                streak++;
                if (streak == 5) return streak;
            }
            best = Math.max(best, streak);
        }

        return best > 1 ? best: -1;
    }
}
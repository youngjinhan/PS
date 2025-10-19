class TopVotedCandidate {
    int[] persons;
    int[] times;
    int[] leading;

    public TopVotedCandidate(int[] persons, int[] times) {
        this.persons = persons;
        this.times = times;
        this.leading = new int[times.length];

        int leader = -1;
        int maxCnt = 0;

        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < persons.length; i++) {
            int newCnt = count.getOrDefault(persons[i], 0) + 1;
            count.put(persons[i], newCnt);

            if (newCnt >= maxCnt) {
                leader = persons[i];
                maxCnt = newCnt;
            }

            leading[i] = leader;
        }
        
    }
    
    public int q(int t) {
        int start = 0, end = persons.length - 1;

        while (start < end) {
            int mid = (start + end + 1) / 2;

            if (times[mid] > t) {
                end = mid - 1;
            } else {
                start = mid;
            }
        }
        return leading[start];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
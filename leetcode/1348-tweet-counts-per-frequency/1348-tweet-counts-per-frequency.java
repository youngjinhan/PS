class TweetCounts {
    private Map<String, List<Integer>> tweets;
    public TweetCounts() {
        this.tweets = new HashMap<>();
    }
    
    public void recordTweet(String tweetName, int time) {
        tweets.computeIfAbsent(tweetName, k -> new ArrayList<>())
        .add(time);
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        List<Integer> tweetTimes = tweets.get(tweetName);
        int chunk;
        if (freq.equals("minute")) {
            chunk = 60;
        } else if (freq.equals("hour")) {
            chunk = 3600;
        } else {
            chunk = 86400;
        }

        int buckets = (endTime - startTime) / chunk + 1;
        int[] res = new int[buckets];
        for (Integer time: tweetTimes) {
            if (time < startTime || time > endTime) continue;
            int i = (time - startTime) / chunk;
            res[i]++;
        }
        
        List<Integer> counts = new ArrayList<>(buckets);
        for (int v : res) counts.add(v);
        return counts;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
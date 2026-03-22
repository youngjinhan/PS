class StockPrice {
    private Map<Integer, Integer> timePriceMap;
    private TreeMap<Integer, Integer> priceCountMap;
    private int currentTime;

    public StockPrice() {
        timePriceMap = new HashMap<>();
        priceCountMap = new TreeMap<>();
    }
    
    public void update(int timestamp, int price) {
        if (timePriceMap.containsKey(timestamp)) {
            int oldPrice = timePriceMap.get(timestamp);
            int count = priceCountMap.get(oldPrice);

            if (count == 1) {
                priceCountMap.remove(oldPrice);
            } else {
                priceCountMap.put(oldPrice, count - 1);
            }
        }

        timePriceMap.put(timestamp, price);
        priceCountMap.put(price, priceCountMap.getOrDefault(price, 0) + 1);
    
        if (timestamp > currentTime) currentTime = timestamp;
    }
    
    public int current() {
        return timePriceMap.get(currentTime);
    }
    
    public int maximum() {
        return priceCountMap.lastKey();
    }

    public int minimum() {
        return priceCountMap.firstKey();
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
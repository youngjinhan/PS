/** 
    참고 풀이
   https://leetcode.com/problems/stock-price-fluctuation/solutions/1514021/java-68-ms-faster-than-100-using-2-prior-dsw9
 */

class StockRecord {
    int timestamp;
    int price;
    
    public StockRecord(){}
    
    public StockRecord(int t, int p) {
        timestamp = t;
        price = p;
    }
}

class StockPrice {
    
    PriorityQueue<StockRecord> max = new PriorityQueue<>((sr1, sr2) -> (sr2.price - sr1.price));
    PriorityQueue<StockRecord> min = new PriorityQueue<>((sr1, sr2) -> (sr1.price - sr2.price));
    StockRecord current_record;
    Map<Integer, Integer> map = new HashMap<>();

    
    public StockPrice() {
        current_record = new StockRecord();
    }
    
    public void update(int timestamp, int price) {
        if(timestamp >= current_record.timestamp) {
            current_record.timestamp = timestamp;
            current_record.price = price;
        }
        
        StockRecord sr = new StockRecord(timestamp, price);
        max.add(sr);
        min.add(sr);
        map.put(timestamp, price);
    }
    
    public int current() {
        return current_record.price;
    }
    
    public int maximum() {
        StockRecord sp = max.peek();
        while(true) {
            sp = max.peek();
            if(sp.price != map.get(sp.timestamp))
                max.poll();
            else break;
        }
        return sp.price;
    }
    
    public int minimum() {
        StockRecord sp = min.peek();
         while(true) {
            sp = min.peek();
            if(sp.price != map.get(sp.timestamp))
                min.poll();
            else break;
        }
        return sp.price;
    }
}

/** 내 풀이 

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

*/

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */

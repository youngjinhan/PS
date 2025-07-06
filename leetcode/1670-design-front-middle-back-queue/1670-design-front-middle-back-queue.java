class FrontMiddleBackQueue {
    private Deque<Integer> firstHalfQueue;
    private Deque<Integer> secondHalfQueue;

    public FrontMiddleBackQueue() {
        this.firstHalfQueue = new ArrayDeque<>();
        this.secondHalfQueue = new ArrayDeque<>();
    }
    
    public void pushFront(int val) {
        this.firstHalfQueue.offerFirst(val);
        if (firstHalfQueue.size() - secondHalfQueue.size() >= 1) {
            int firstLast = firstHalfQueue.pollLast();
            secondHalfQueue.offerFirst(firstLast);
        }
    }
    
    public void pushMiddle(int val) {
        if (firstHalfQueue.size() > 0 && secondHalfQueue.size() == 0) {
            int firstLast = firstHalfQueue.pollLast();
            secondHalfQueue.offer(firstLast);
        }
        
        if (firstHalfQueue.size() < secondHalfQueue.size()) firstHalfQueue.offer(val);
        else secondHalfQueue.offerFirst(val);

        // if (firstHalfQueue.size() - secondHalfQueue.size() >= 2) {
        //     int firstLast = firstHalfQueue.pollLast();
        //     secondHalfQueue.offerFirst(firstLast);
        // }
    }
    
    public void pushBack(int val) {
        secondHalfQueue.offer(val);
        if (secondHalfQueue.size() - firstHalfQueue.size() >= 2) {
            int secondFirst = secondHalfQueue.pollFirst();
            firstHalfQueue.offer(secondFirst);
        }
    }
    
    public int popFront() {
        if (firstHalfQueue.size() == 0 && secondHalfQueue.size() == 0) return -1;
        if (firstHalfQueue.size() == 0) return secondHalfQueue.pollFirst();
        int front = firstHalfQueue.pollFirst();

        if (firstHalfQueue.size() + 2 == secondHalfQueue.size()) {
            int secondFirst = secondHalfQueue.pollFirst();
            firstHalfQueue.offer(secondFirst);
        }
        return front;
    }
    
    public int popMiddle() {
        if (firstHalfQueue.size() == 0 && secondHalfQueue.size() == 0) return -1;
        if (firstHalfQueue.size() == secondHalfQueue.size()) {
            return firstHalfQueue.pollLast();
        } else {
            return secondHalfQueue.pollFirst();
        }
    }
    
    public int popBack() {
        if (firstHalfQueue.size() == 0 && secondHalfQueue.size() == 0) return -1;
        int back = secondHalfQueue.pollLast();
        if (firstHalfQueue.size() > secondHalfQueue.size()) {
            int firstLast = firstHalfQueue.pollLast();
            secondHalfQueue.offerFirst(firstLast);
        }
        return back;
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param_4 = obj.popFront();
 * int param_5 = obj.popMiddle();
 * int param_6 = obj.popBack();
 */

//  885613, 411268, 508187, 772690, 375192, 888438


// 885613 411268 772690
// 375192 888438
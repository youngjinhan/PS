class MyCircularQueue {
    private int[] space;
    private int added;
    private int front = -1;
    private int cur = -1;

    public MyCircularQueue(int k) {
        space = new int[k];
        Arrays.fill(space, -1);
    }
    
    public boolean enQueue(int value) {
        int k = space.length;
        if (space[(cur + 1) % k] > -1) return false;
        cur = (cur + 1) % k;
        space[cur] = value;
        if (front == -1) front++;
        added++;
        return true;
    }
    
    public boolean deQueue() {
        if (front == -1 || space[cur] == -1) return false;
        space[front++] = -1;
        int k = space.length;
        front %= k;
        added--;
        return true;
    }
    
    public int Front() {
        if (front == -1) return -1;
        return space[front];
    }
    
    public int Rear() {
        if (cur == -1) return -1;
        return space[cur];
    }
    
    public boolean isEmpty() {
        return added == 0;
    }
    
    public boolean isFull() {
        int k = space.length;
        return added == k;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
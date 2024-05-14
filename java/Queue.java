class Queue {
    int n = 0; int[] array = new int[5];
    int front = -1, rear = -1;

    void display() {
        for (int i = 0; i < n; i++)
            System.out.printf("%d ", array[i]);
    }

    void push(int item) {
        if (rear == 4) {
            System.out.println("overflow!");
            return;
        }

        if (front == -1) front = 0;
        array[n++] = item;
    }

    int remove() {
        if (front == -1) {
            System.out.println("underflow!");
            return 0;
        }
        if (front >= rear) {
            front = -1;
            rear = -1;
        } else front++;
        return array[n--];
    }

    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(2);
        stack.push(3);
        stack.pop();
        stack.push(4);
        stack.display();
    }
}

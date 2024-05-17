class Queue {
    int[] array = new int[5];
    int front = -1, rear = -1;

    void display() {
        for (int i = front; i <= rear; i++)
            System.out.printf("%d ", array[i]);
    }

    void enque(int item) {
        if (rear == 4) {
            System.out.println("overflow!");
            return;
        }

        if (front == -1) front++;
        array[++rear] = item;
    }

    void remove() {
        if (front == -1) {
            System.out.println("underflow!");
            return;
        }
        if (front >= rear) {
            front = -1;
            rear = -1;
        } else front++;
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enque(2);
        queue.enque(3);
        queue.enque(4);
        queue.enque(5);
        queue.enque(6);
        queue.enque(0);
        //queue.remove();
        queue.display();
    }
}

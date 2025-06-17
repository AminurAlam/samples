class Stack {
    int n = 0; int[] array = new int[5];

    void display() {
        for (int i = 0; i < n; i++)
            System.out.printf("%d ", array[i]);
    }

    void push(int item) {
        if (n == 5) {
            System.out.println("overflow!");
            return;
        }
        array[n++] = item;
    }

    int pop() {
        if (n == 0) {
            System.out.println("overflow!");
            return 0;
        }
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

class assignment_3 {
    static void func() {
        System.out.println("method was called");
    }
    public static void main(String args[]) {
        // Count t1 = new Count();
        // Count t2 = new Count();
        // Count t3 = new Count();
        func();
    }
}

class Count {
    static int count = 0;

    { count++; }
}

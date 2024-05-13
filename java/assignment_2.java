public class assignment_2 {
    public static void main(String[] args) {
        // System.out.println(
        //     "sum is: " +
        //     Integer.parseInt(args[0]) +
        //     Integer.parseInt(args[1])
        // );

        // Add mix = new Add();
        // int i = 8;
        // double d = 16;
        // String s = "foo";
        //
        // System.out.println(mix.add(i, i));
        // System.out.println(mix.add(i, d));
        // System.out.println(mix.add(d, d));
        // System.out.println(mix.add(s, s));

        // Mod obj = new Mod(3);
        // int val = 5;
        // System.out.printf("val, ref: %d, %d\n", val, obj.n);
        // obj.inc_val(val);
        // obj.inc_ref(obj);
        // System.out.printf("val, ref: %d, %d\n", val, obj.n);
    }
}

class SumInput {
    public static void main(String[] args) {
        System.out.println(
            "sum is: " +
            Integer.parseInt(args[0]) +
            Integer.parseInt(args[1])
        );
    }
}

class Add {
    int add(int a, int b) { return a + b; };
    double add(int a, double b) { return a + b; };
    double add(double a, double b) { return a + b; };
    String add(String a, String b) { return a + b; };
}

class Mod {
    int n;

    Mod(int a) { n = a; }

    void inc_val(int n) { n++; }
    void inc_ref(Mod o) { o.n++; }
}

class assignment_1 {
    public static void main(String[] args) {
        // CheckPrime prime = new CheckPrime();
        // System.out.println(prime.check(6) ? "prime" : "not prime");

        // Factorial factorial = new Factorial();
        // System.out.println(factorial.loop(5));
        // System.out.println(factorial.recurse(4));

        // Complex foo = new Complex(12, 6);
        // Complex bar = new Complex(4, 3);
        // foo.add(bar).show(); // foo + bar = 16 + 9i
        // foo.sub(bar).show(); // foo - bar = 8 + 3i
        // foo.mul(bar).show(); // foo * bar = 30 + 60i
    }
}

class CheckPrime {
    boolean check(int num) {
        for (int i = 2; i < num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

class Factorial {
    int loop(int num) {
        int sum = 1;
        for (int i = 2; i <= num; i++) sum *= i;

        return sum;
    }

    int recurse(int num) {
        if (num == 1) { return 1; }
        return num * recurse(num-1);
    }
}

class Complex {
    int real, imag;

    Complex(int r, int i) {
        real = r;
        imag = i;
    }

    Complex add(Complex that) {
        return new Complex(
            this.real + that.real,
            this.imag + that.imag
        );
    }

    Complex sub(Complex that) {
        return new Complex(
            this.real - that.real,
            this.imag - that.imag
        );
    }

    Complex mul(Complex that) {
        return new Complex(
            this.real * that.real - this.imag * that.imag,
            this.real * that.imag + this.imag * that.real
        );
    }

    void show() {
        System.out.println(this.real + " + " + this.imag + "i");
    }
}

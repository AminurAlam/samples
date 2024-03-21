class assignment_1 {
    public static void main(String[] args) {
        CheckPrime prime = new CheckPrime();
        System.out.println(prime.check(6) ? "prime" : "not prime");

        Factorial factorial = new Factorial();
        System.out.println("factorial is " + factorial.loop(5));
        System.out.println("factorial is " + factorial.recurse(5));

        Complex foo = new Complex(1, 2);
        Complex bar = new Complex(3, 1);
        foo.add(bar); // foo + bar
        foo.sub(bar); // foo - bar
        foo.mul(bar); // foo * bar
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
        for (int i = 2; i <= num; i++) 
            sum *= i;

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
            this.real * that.real,
            this.imag * that.imag
        );
    }
}

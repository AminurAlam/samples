#include <math.h>
#include <stdio.h>

// calculate simple intrest
void simple_intrest() {
    double p, r, t, si;
    printf("enter principal, rate, time: ");
    scanf("%lf %lf %lf", &p, &r, &t);

    si = ((p * r * t) / 100);

    printf("%f is the simple intrest\n", si);
}

// calculate simple intrest using a function
double get_simple_intrest(double p, double r, double t) {
    return ((p * r * t) / 100);
}

// calculate compound intrest
void compound_intrest() {
    double p, r, t, ammount, ci;
    printf("enter principal, rate, time: ");
    scanf("%lf %lf %lf", &p, &r, &t);

    ammount = p * ((pow((1 + r / 100), t)));
    ci = ammount - p;

    printf("Compound Interest is : %f", ci);
}

// get ascii value of a character
void get_ascii() {
    char c;
    printf("enter a char: ");
    scanf("%c", &c);
    printf("ascii val of %c is %d\n", c, c);
}

// find area of a rectangle
void get_rectangle_area() {
    int l, b;
    printf("enter length, breadth: ");
    scanf("%d %d", &l, &b);

    printf("area is %d\n", l * b);
}

// find area of a square
void get_square_area() {
    int s;
    printf("enter side of square: ");
    scanf("%d", &s);

    printf("area is %d\n", s * s);
}

// find area of a circle
void get_circle_area(int radius) {
    printf("area is %f\n", 3.14 * radius * radius);
}

// find sum of prime numbers between 100 and 500
void prime() {
    int start = 100, end = 500;
    int i, j, check, collect = 0;

    for (i = start; i <= end; i++) {
        for (j = 2; j < i; j++) {
            check = 0;
            if (i % j == 0) {
                check = 1;
                break;
            }
        }
        if (!check) collect += i;
    }
    printf("sum of primes between %d and %d is %d\n", start, end, collect);
}

// find if a number is odd or even
void odd_even(int num) {
    printf("%3d is %s\n", num, (num % 2 == 0 ? "even" : "odd"));
}

// swap values of two variables
void swap(int a, int b) {
    printf("a = %d, b = %d\n", a, b);
    int temp = a;
    a = b;
    b = temp;
    printf("a = %d, b = %d\n", a, b);
}

// check if a number is palindrome or not
void palindrome() {
    int num, num_copy, num_reverse = 0;
    printf("enter an integer: ");
    scanf("%d", &num);
    num_copy = num;

    while (num) {
        num_reverse = (num_reverse * 10) + (num % 10);
        num /= 10;
    }

    if (num_copy == num_reverse) printf("%d is a palindrome\n", num_copy);
    else printf("%d is not a palindrome\n", num_copy);
}

// generate fibonacci series
void fib() {
    int end, n1 = 0, n2 = 1, n3;
    printf("enter end of sequence: ");
    scanf("%d", &end);
    printf("%d %d ", n1, n2);

    while (end) {
        n3 = n1 + n2;
        printf("%d ", n3);
        n1 = n2;
        n2 = n3;
        end--;
    }
}

// convert binary number to decimal number
void bin_to_dec() {
    long num, rem, dec = 0;
    printf("enter number: ");
    scanf("%ld", &num);

    for (int i = 0; num; i++) {
        rem = num % 10;
        num /= 10;
        dec += rem * pow(2, i);
    }

    printf("%ld\n", dec);
}

// find average of marks
void avg() {
    float avg, entry, count = 0, sum = 0;
    printf("enter score below (-ve to end)\n");

    for (entry = 0; 0 <= entry; count++) {
        scanf("%f", &entry);
        sum += entry;
    }

    avg = (sum - entry) / (count - 1);
    printf("average is: %.2f\n", avg);
}

// find factorial of a number
int factorial(int i) {
    if (i < 2) {
        return i;
    }
    return i * factorial(i - 1);
}

int main() {
    // simple_intrest();
    // printf("%lf\n", get_simple_intrest(1000, 1, 1));
    // compound_intrest();
    // get_ascii();
    // get_rectangle_area();
    // get_square_area();
    // get_circle_area();
    // prime();
    // for (int i = 1; i <= 10; i++) { odd_even(i); }
    // swap(10, 12);
    // palindrome();
    // fib();
    // bin_to_dec();
    // avg();
    // printf("factorial is %d\n", factorial(5));
    return 0;
}

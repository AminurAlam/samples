#include <math.h>
#include <stdio.h>

// calculate simple intrest
void simple_intrest() {
    double p, r, t, si;
    printf("enter principal, rate, time: ");
    scanf("%lf %lf %lf", &p, &r, &t);

    si = ((p * r * t) / 100) - p;

    printf("%f is the simple intrest\n", si);
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

int main() {
    // simple_intrest();
    // get_ascii();
    // get_rectangle_area();
    // get_square_area();
    for (int i = 1; i <= 10; i++) { odd_even(i); }
    prime();
    swap(10, 12);
    return 0;
}

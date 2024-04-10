#include <math.h>
#include <stdio.h>

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

// calculate simple intrest
double get_simple_intrest(double p, double r, double t) {
    return (p * r * t) / 100;
}

void simple_intrest() {
    double p, r, t, si;
    printf("enter principal, rate, time: ");
    scanf("%lf %lf %lf", &p, &r, &t);

    si = get_simple_intrest(p, r, t);

    printf("%f is the simple intrest\n", si);
}

// calculate compound intrest
void compound_intrest() {
    double p, r, t, ammount, ci;
    printf("enter principal, rate, time: ");
    scanf("%lf %lf %lf", &p, &r, &t);

    ammount = p * pow(1 + r / 100, t);
    ci = ammount - p;
    printf("Compound Interest is : %f", ci);
}

// use getchar and putchar
// use gets and puts

// display two strings
void distr() {
    char str1[32], str2[32];
    printf("enter first string: ");
    scanf("%s", str1);
    printf("enter second string: ");
    scanf("%s", str2);

    printf("%s\n%s\n", str1, str2);
}

// get ascii value of a character
void get_ascii() {
    printf("enter a char: ");
    char c = getchar();
    // scanf("%c", &c);
    printf("ascii val of %c is %d\n", c, c);
}

// find sum of prime numbers between 100 and 500
void prime() {
    int num, check = 1;
    printf("enter a number: ");
    scanf("%d", &num);

    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) { check = 0; }
    }

    if (check) printf("prime\n");
    else printf("not prime\n");
}

// find sum of prime numbers between 100 and 500
void prime_between() {
    int check, collect = 0;

    for (int i = 100; i <= 500; i++) {
        for (int j = 2; j <= i / 2; j++) {
            check = 1;
            if (i % j == 0) {
                check = 0;
                break;
            }
        }
        if (check) collect += i;
    }

    printf("sum of primes is %d\n", collect);
}

// find if a number is odd or even
void odd_even() {
    int num;
    printf("enter number: ");
    scanf("%d\n", &num);

    if (num % 2 == 0) printf("even\n");
    else printf("even\n");
}

// swap values of two variables
void swap() {
    int a, b;
    printf("enter two numbers:\n");
    scanf("%d %d", &a, &b);

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

    do {
        num_reverse = (num_reverse * 10) + (num % 10);
        num /= 10;
    } while (num);

    if (num_copy == num_reverse) {
        printf("%d is a palindrome\n", num_copy);
    } else {
        printf("%d is not a palindrome\n", num_copy);
    }
}

// generate fibonacci series
void fib(int end) {
    int n1 = 0, n2 = 1, n3;
    printf("%d %d ", n1, n2);

    while (end) {
        n3 = n1 + n2;
        printf("%d ", n3);
        n1 = n2;
        n2 = n3;
        end--;
    }
}

void call_fib() {
    int end;
    printf("enter length: ");
    scanf("%d", &end);
    fib(end);
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
int fact(int i) {
    if (i < 2) { return i; }
    return i * fact(i - 1);
}

// find maximum of three numbers using a function
int max(int a, int b) { return a > b ? a : b; }

void max_of_3() {
    int a, b, c;
    printf("enter three numbers:\n");
    scanf("%d %d %d", &a, &b, &c);

    printf("max is %d\n", max(a, max(b, c)));
}

// 1D array
void array1d() {
    int table[3];
    printf("enter 3 numbers:\n");
    for (int i = 0; i < 3; i++) { scanf("%d", &table[i]); }

    for (int i = 0; i < 3; i++) { printf("%d ", table[i]); }
}

// tree
void tree() {
    for (int i = 1; i < 9; i += 2) {
        for (int p = (10 - i) / 2; p; p--) printf(" ");
        for (int l = 0; l < i; l++) printf("*");
        printf("\n");
    }
}

// read a line of text from the terminal using getchar()
void get_s() {
    int i = 0;
    char str[32];

    while (str[i - 1] != '\n') str[i++] = getchar();

    printf("%s\n", str);
}

// copy one str into another and count the number of chars copied
void copy_of_a() {
    char orig[64], copy[64];
    printf("enter a string: ");
    scanf("%s", orig);

    strcpy(copy, orig);
    printf("copied '%s'\n", copy);
    printf("length is %lu\n", strlen(copy));
}

int main() {
    int a = 0;
    printf("a is at %x\n", &a);
    int b = 0;
    printf("b is at %x\n", &b);
    return 0;
}

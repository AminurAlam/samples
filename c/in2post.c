#include <stdio.h>
#define IS_OPERAND (t >= 'a' && t <= 'z') || (t >= '0' && t <= '9')

// precedence
int prec(char c) {
    if (c == '/' || c == '*') return 2;
    else if (c == '+' || c == '-') return 1;
    return -1;
}

int main() {
    char result[1000], stack[1000], infix[] = "a+b*c+d";
    int r = 0, s = -1;

    for (int i = 0; i < strlen(infix); i++) {
        char t = infix[i];

        if (IS_OPERAND) result[r++] = t;
        else if (t == '(') stack[++s] = t;
        else if (t == ')') {
            while (s >= 0 && stack[s] != '(')
                result[r++] = stack[s--];
            s--;
        } else {
            while (s >= 0 && prec(t) <= prec(stack[s]))
                result[r++] = stack[s--];
            stack[++s] = t;
        }
    }

    while (s >= 0) result[r++] = stack[s--];
    result[r] = '\0';
    printf("%s\n", result);
}

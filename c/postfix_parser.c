#include <stdio.h>
#define TOKEN_IS_OP token == '+' || token == '-' || token == '*' || token == '/'

char stack[100];
int n = 0;
int c_i(char x) { return (int)x - 48; }
void insert(int item) { stack[++n] = (char)item + 48; }
char pop() { return stack[n--]; }

void resolve_token(char token) {
    if (TOKEN_IS_OP) {
        int b = c_i(pop()), a = c_i(pop());

        switch (token) {
        case '+': insert(a + b); break;
        case '-': insert(a - b); break;
        case '*': insert(a * b); break;
        case '/': insert(a / b); break;
        }
    } else insert(c_i(token));
}

int solve_postfix(char post[]) {
    for (int i = 0; i < strlen(post); i++) { resolve_token(post[i]); }
    return c_i(pop());
}

int main() {
    printf("RESULT: %d\n", solve_postfix("12+3+"));   // 6
    printf("RESULT: %d\n", solve_postfix("12-3-"));   // -4
    printf("RESULT: %d\n", solve_postfix("12*3*"));   // 6
    printf("RESULT: %d\n", solve_postfix("62/"));     // 3
    printf("RESULT: %d\n", solve_postfix("231*+9-")); // -4
}

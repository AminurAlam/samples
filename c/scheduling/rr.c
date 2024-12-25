#include <stdio.h>

int main() {
    int n, tq, clock = 0, total_tat = 0, max_bt = 0;
    printf("tq: ");
    scanf("%d", &tq);
    printf("ps: ");
    scanf("%d", &n);
    int bt[n];

    for (int i = 0; i < n; i++) {
        printf("bt[%d]: ", i);
        scanf("%d", &bt[i]);
        if (bt[i] > max_bt) max_bt = bt[i];
    }

    for (int j = 0; j < max_bt; j += tq) {
        for (int i = 0; i < n; i++) {
            if (bt[i] <= 0) continue;
            if (bt[i] > tq) clock += tq;
            else {
                clock += bt[i];
                total_tat += clock;
            }
            bt[i] -= tq;
        }
    }

    printf("avg tat: %f\n", (double)total_tat / n);

    return 0;
}

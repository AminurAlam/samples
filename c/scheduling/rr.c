#include <stdio.h>

int main() {
    int n, tq, max_bt = 0, clock = 0;
    double total_tat = 0;
    printf("enter time quantum: ");
    scanf("%d", &tq);
    printf("enter num of processes: ");
    scanf("%d", &n);
    int bt[n], tat[n];

    for (int i = 0; i < n; i++) {
        printf("enter burst time for %d: ", i);
        scanf("%d", &bt[i]);
    }

    for (int i = 0; i < n; i++)
        if (bt[i] > max_bt) max_bt = bt[i];

    for (int j = 0; j < max_bt; j += tq) {
        for (int i = 0; i < n; i++) {
            if (bt[i] <= 0) continue;
            if (bt[i] > tq) clock += tq;
            else {
                clock += bt[i];
                tat[i] = clock;
                total_tat += clock;
            }
            bt[i] -= tq;
        }
    }

    printf("avg tat: %f\n", total_tat / n);

    return 0;
}

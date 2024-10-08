#include <stdio.h>

int main() {
    int n;
    printf("enter num of processes: ");
    scanf("%d", &n);
    int bt[n], wt[n], tat[n], temp;

    for (int i = 0; i < n; i++) {
        printf("enter burst time for %d: ", i);
        scanf("%d", &bt[i]);
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (bt[j] > bt[j + 1]) {
                temp = bt[j];
                bt[j] = bt[j + 1];
                bt[j + 1] = temp;
            }
        }
    }

    wt[0] = 0, tat[0] = bt[0];
    double totatl_wt = 0, total_tat = tat[0];

    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
        totatl_wt += wt[i];
        total_tat += wt[i] + bt[i];
    }

    printf("avg tat: %f\n", total_tat / n);
    printf("avg wt: %f\n", totatl_wt / n);

    return 0;
}

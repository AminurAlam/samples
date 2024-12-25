#include <stdio.h>

int main() {
    int n;
    printf("enter num of processes: ");
    scanf("%d", &n);
    int bt[n], wt[n], temp;

    for (int i = 0; i < n; i++) {
        printf("bt[%d]: ", i);
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

    wt[0] = 0;
    int total_wt = 0, total_tat = bt[0];

    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
        total_wt += wt[i];
        total_tat += wt[i] + bt[i];
    }

    printf("avg tat: %f\n", (double)total_tat / n);
    printf("avg wt: %f\n", (double)total_wt / n);

    return 0;
}

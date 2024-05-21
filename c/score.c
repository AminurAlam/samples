#include <stdio.h>
#define MAX_STUDENT 5
#define MAX_SUBJECT 3

int A[MAX_STUDENT][MAX_SUBJECT];

int main() {
    for (int i = 0; i < MAX_STUDENT; i++) {
        printf("for student %d\n", i);
        printf("enter score1, score2, score3: ");
        scanf("%d %d %d", &A[i][0], &A[i][1], &A[i][2]);
    }

    int max[] = {0, 0, 0};
    int sum[] = {0, 0, 0};

    for (int i = 0; i < MAX_STUDENT; i++) {
        for (int j = 0; j < MAX_SUBJECT; j++) {
            if (max[j] < A[i][j]) max[j] = A[i][j];
            sum[j] += A[i][j];
        }
    }

    printf("\nhighest score in each subject is:\n");
    printf("%d %d %d\n", max[0], max[1], max[2]);

    printf("\naverage in each subject is:\n");
    printf("%f %f %f\n", (float)sum[0] / 5, (float)sum[1] / 5, (float)sum[2] / 5);

    return 0;
}

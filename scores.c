#include <stdio.h>
#include <stdlib.h>
float average (int array [], int n);

int main (void)
{
    const int n = 3;
    int scores [n];
    for (int i = 0; i < n; i++)
    {
        printf("Enter score %d: ", i +1);
        scanf("%d", &scores[i]);
    }
    printf("The average of scores is: %f\n", average(scores, n));
}

float average (int array [], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += array[i];
    }
    return (float) sum / 3;
}
#include <stdio.h>
#include <stdlib.h>
void printGrid (int size);
int getSize(void);

int main(void)
{
    //Get size brick
    int n = getSize();
    //Print grid of bricks
    printGrid(n);
}

int getSize(void)
{
    int n;
    do
    {
        printf("Enter the size: ");
        scanf("%d", &n);
    }
    while (n < 1);
}

void printGrid (int size)
{
    for(int i=0; i < size; i++)
    {
        for (int j = 0; j < size ; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
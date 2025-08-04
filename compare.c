#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    int a,b;
    printf("Value of a: ");
    scanf("%d", &a);
    
    printf("Value of b: ");
    scanf("%d", &b);
    
    if(a < b)
        printf("%d is less than %d\n",a,b);
    
    else if (a>b)
        printf("%d is major than %d\n",a,b);
    
    else
        printf("%d is equal to %d\n",a,b);
    
} 
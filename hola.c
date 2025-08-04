#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main (void)
{
    char name[100];
    printf("Hello, world\n");
    printf("What's your name? ");
    fgets(name, sizeof(name), stdin);
    printf("Hello, %s\n", name);
    return 0;
}
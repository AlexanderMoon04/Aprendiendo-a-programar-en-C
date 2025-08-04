#include <stdio.h>
#include <stlib.h>

int main (void)
{
    int *list = malloc(3 * sizeof(int)); //malloc gives a chunk of memory
    if (list == NULL)
        return 1;

    list[0]=1;
    list[1]=2;
    list[2]=3;

    int *tmp =realloc (list, 4* sizeof(int));
    if (tmp == Null)
    {
        free(list); //avoid memory leak, always free memory
        return 1;
    }
    
    tmp[3] = 4;

    free(list);

    list = tmp;

    for (int i=0; i<4; i++)
    {
        printf("%i", list[i])
    }

}
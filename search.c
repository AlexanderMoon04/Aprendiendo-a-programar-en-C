#include <stdio.h>
#include <stdlib.h>
#include <string.h> //Functions to strings like compare

typedef struct {
    char *name;
    char *number;
}
person;

int main (void)
{

    person people[2];

    people[0].name ="Yonsina";
    people[0].number = "61429288349";

    people[1].name = "Darkar";
    people[1].number = "666";

    const char *strings[] = {"tilin", "tilina", "tilino", "tilinito","tilinote","xd"};
    char name[30];
    printf("Enter a name: ");
    scanf("%29s", name);

    int n = sizeof(strings)/sizeof(strings[0]);
    for(int i = 0 ; i < n; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("%s was found at index %d\nNumber is: %s\n", name, i,people[i].number);
            return 0;
        }
    }
    printf("%s was not found\n",name);
    return 1;
}
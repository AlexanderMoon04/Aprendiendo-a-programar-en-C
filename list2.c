#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}node;

int main (void)
{
    //Memory for numbers
    node *list =NULL;

    int a;
    //build list
    for(int i = 0;i < 3;i++)
    {
        //Allocate node for number
        node *n = malloc(sizeof(node));
        if(n==NULL)
        {
            return 1;
        }
        printf("Number: ");
        scanf("%i",&a);
        n->number = a;
        n->next = NULL;

        //if list is empty
        if (list == NULL)
        {
            list =n;
        }
        
        //if number belongs at beginning of list
        else
        {
            for (node *ptr =list;ptr != NULL; ptr = ptr->next)
            {
                if(ptr->next ==NULL)
                {
                    //append node
                    ptr->next =n;
                    break;
                }
            }
        }
    }
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr ->number);
    }
  
    node *ptr =list;
    while (ptr !=NULL) //undo all of the node one by one
    {
        node *next = ptr ->next;
        free(ptr);
        ptr = next;
    }
    return 0;   
}
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
struct node
{
    char nm[30];
    struct node *link;
}*head = NULL,*temp,*p;
void display()
{
    temp = (struct node *)malloc(sizeof(struct node));
    if(head == NULL)
        printf("No Elements Present");
    else
    {
        temp = head;
        while(temp)
        {
            printf("%s\t",temp->nm);
            temp = temp->link;
        }
    }
}

void input()
{   
    temp = (struct node *)malloc(sizeof(struct node));
    printf("Enter filename");
    scanf("%s",temp->nm);
    temp->link = NULL;
    if(head == NULL)
        head = temp;
    else
    {
        struct node *p;
        p = (struct node *)malloc(sizeof(struct node));
        p = head;
        while(p->link)
            p = p->link;
        p->link = temp;
    }
}

void delete()
{
    printf("Enter filename\n");
    char k[30];
    scanf("%s", k);
    struct node *temp = head;
    if (strcmp(temp->nm, k) == 0)
    {
        head = temp->link;
        printf("File deleted\n");
        return;
    }
    while (temp != NULL && temp->link != NULL)
    {
        if (strcmp(temp->link->nm, k) == 0)
        {
            temp->link = temp->link->link;
            printf("File deleted.\n");
            return;
        }
        temp = temp->link;
    }
    printf("File not found\n");
}

void main()
{
    int n;
    char t = 'y';
    while(true) 
    {
        printf("\nEnter a choice");
        printf("\n 1.Enter a file \n 2.Display all files \n 3.Delete a file");
        scanf("%d",&n);
        switch (n)
        {
        case 1:
            input();
            break;
        case 2:
            display();
            break;
        case 3:
            delete();
            break;
        default:
            exit(0);
        }
    }
}